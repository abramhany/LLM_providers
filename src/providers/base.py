from abc import ABC ,abstractmethod
from config.config import Config
from schema.chat import Chat
class LLMbase(ABC):

    @abstractmethod
    def __init__(self,*,Config:Config) -> None:
        super().__init__()
   
    @abstractmethod
    def chat(self,*,chat_input:Chat)->(str|None):
        """Text Generation for valid requests"""
        pass