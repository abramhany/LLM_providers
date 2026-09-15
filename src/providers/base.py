from abc import ABC ,abstractmethod
from config.config import Config

class LLMbase(ABC):

   
    @abstractmethod
    def chat(self)->(str|None):
        pass