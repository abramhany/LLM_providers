from abc import ABC ,abstractmethod
from config.config import Config
from schema import Chat , Ticket
from pydantic import BaseModel

class LLMbase(ABC):

    @abstractmethod
    def __init__(self,*,Config:Config) -> None:
        super().__init__()
   
    @abstractmethod
    def generation(self,*,chat_input:Chat)->(str|None):
        """Text Generation for valid requests"""
        pass

    def structured_generation(self,*,chat_input:Chat)->(BaseModel | None):
        """Structured text Generation for valid requests"""
        pass