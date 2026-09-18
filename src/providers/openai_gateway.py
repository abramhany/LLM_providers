from pydantic import BaseModel

from schema.ticket import Ticket

from .base import LLMbase
from config.config import Config
from openai import (OpenAI,APIConnectionError,APITimeoutError,AuthenticationError,RateLimitError,BadRequestError)
from schema.chat import Chat
from exceptions.exceptions import (InvalidRequest_Error,Provider_Error,Authentication_Error,Connection_Error,RateLimit_Error,BadRequest_Error)
from enums.llm_error import LLMError
import json




class OpenAIGateway(LLMbase):

    def __init__(self,config:Config) -> None:
        
        self.client = OpenAI(api_key=config.groq_api_key,
                             base_url=config.base_url,
                             timeout=config.timeout)
        
        self.model = config.model_name
        


    def generation(self,*,chat_input:Chat)->(str|None):

        param = {

            'model': self.model,
            'messages':[{'role':message.role.value,'content':message.content} for message in chat_input.messages],
            'temperature': chat_input.temperature,
            "max_tokens": chat_input.max_new_tokens,
        }

        if chat_input.top_p is not None :

            param['top_p'] = chat_input.top_p

        if chat_input.top_k is not None :
            raise InvalidRequest_Error(LLMError.UNSUPPORTED_PARAMETER)
    
    
        response = self._run(self.client.chat.completions.create,**param)
        content = response.choices[0].message.content

        if content is None :

            raise Provider_Error(LLMError.EMPTY_RESPONSE)

        return content

          
    def structured_generation(self, *, chat_input: Chat) -> BaseModel | None:
            param = {
            
                        'model': self.model,
                        'input':[{'role':message.role.value,'content':message.content} for message in chat_input.messages],
                        'temperature': chat_input.temperature,
                        "text_format": chat_input.text_format
                    }
        
            response = self._run(self.client.responses.parse,**param)
            content = response.output_parsed
            if content is None :
                raise Provider_Error(LLMError.EMPTY_RESPONSE)
            try:
                content = content.model_dump_json()
                json.loads(content)
            except json.JSONDecodeError as e:
                raise e
            
            return content
        
        


    def _run(self,fn,*args,**kargs):
        try:
            return fn(*args,**kargs)
        except (APIConnectionError,APITimeoutError) as e:
                raise Connection_Error(LLMError.CONNECTION_ERROR) from e
        except AuthenticationError as e :
                raise Authentication_Error(LLMError.AUTENTICATION_ERROR) from e
        except RateLimitError as e:
                raise RateLimit_Error(LLMError.RATE_LIMIT_EXCEEDED) from e
        except BadRequestError as e :
                raise BadRequest_Error(LLMError.INVALID_REQUEST) from e
        