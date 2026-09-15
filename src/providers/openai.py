from .base import LLMbase
from config.config import Config
from openai import OpenAI



class Openai(LLMbase):

    def __init__(self,config:Config) -> None:
        self.client = OpenAI(api_key=config.groq_api_key,base_url=config.base_url)
        self.model = config.model_name


    def chat(self)->(str|None):
        chat = self.client.chat.completions.create(model=self.model,messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},])

        return chat.choices[0].message.content