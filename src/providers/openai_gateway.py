from .base import LLMbase
from config.config import Config
from openai import OpenAI
from schema.chat import Chat


class Openai_gateway(LLMbase):

    def __init__(self,config:Config) -> None:
        self.client = OpenAI(api_key=config.groq_api_key,base_url=config.base_url,timeout=config.timeout)
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
            param['top_k'] = chat_input.top_k

        response = self.client.chat.completions.create(**param)

        return response.choices[0].message.content