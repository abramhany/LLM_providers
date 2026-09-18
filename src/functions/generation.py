import logging 
from providers.openai_gateway import Openai_gateway 
from providers.gateway import Gateway
from config.config import Config
from schema import Chat , Message , Ticket
from enums.roles import Role
from prompt.summarizer import summary_prompt




class Generation():
    def __init__(self) -> None:
        self.config = Config()

    def chat(self,user_prompt:str):
        
        message_list =[ Message(role=Role.SYSTEM,content=sum_prompt),Message(role=Role.USER,content='My laptop broke and i cant do my home work')]



sum_prompt = summary_prompt()

gateway = Gateway(Config=settings,llm_provider=Openai_gateway(config=settings))




chat = Chat(messages=message_list,text_format=Ticket)
response = gateway.generation(chat_input=chat)



print(response)
