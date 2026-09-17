from abc import ABC ,abstractmethod
from config.config import Config
from schema import Chat , Ticket


class LLMbase(ABC):

    @abstractmethod
    def __init__(self,*,Config:Config) -> None:
        super().__init__()
   
    @abstractmethod
    def generation(self,*,chat_input:Chat)->(str|None):
        """Text Generation for valid requests"""
        pass

    