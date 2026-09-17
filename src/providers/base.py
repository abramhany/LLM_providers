from abc import ABC ,abstractmethod
from config.config import Config
from schema import Chat , Ticket


class LLMbase(ABC):

    @abstractmethod
    def __init__(self,*,Config:Config) -> None:
        super().__init__()
   
    @abstractmethod
    def chat(self,*,chat_input:Chat)->(str|None):
        """Text Generation for valid requests"""
        pass

    @abstractmethod
    def sturctured_ouput(self,*,ticket:Ticket,chat_input:Chat):
        '''Returned a sturcured_output_based on the prompt and the message'''
        pass