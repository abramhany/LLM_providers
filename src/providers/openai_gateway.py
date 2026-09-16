from .base import LLMbase
from config.config import Config
from openai import (OpenAI,APIConnectionError,APITimeoutError,AuthenticationError,RateLimitError,BadRequestError)
from schema.chat import Chat
from exceptions.exceptions import (InvalidRequest_Error,Provider_Error,Authentication_Error,Connection_Error,RateLimit_Error,BadRequest_Error)
from enums.llm_error import LLMError



class Openai_gateway(LLMbase):

    def __init__(self,config:Config) -> None:
        
        self.client = OpenAI(api_key=config.groq_api_key,
                             base_url=config.base_url,
                             timeout=config.timeout)
        
        self.model = config.model_name
        


    def chat(self,chat_input:Chat)->(str|None):

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
        try:

            response = self.client.chat.completions.create(**param)
            content = response.choices[0].message.content

            if content is None :

                raise Provider_Error(LLMError.EMPTY_RESPONSE)

            return content
        
        except (APIConnectionError,APITimeoutError) as e:
            raise Connection_Error(LLMError.CONNECTION_ERROR) from e
        except AuthenticationError as e :
            raise Authentication_Error(LLMError.AUTENTICATION_ERROR) from e
        except RateLimitError as e:
            raise RateLimit_Error(LLMError.RATE_LIMIT_EXCEEDED) from e
        except BadRequestError as e :
            raise BadRequest_Error(LLMError.RATE_LIMIT_EXCEEDED) from e
        
        

