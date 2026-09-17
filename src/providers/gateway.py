from config.config import Config
import random
from .base import LLMbase
from exceptions.exceptions import Connection_Error,RateLimit_Error  , Provider_Error , Authentication_Error
from schema.chat import Chat
from enums.llm_error import LLMError
import time
import logging

logging.basicConfig(level=logging.INFO, filename='info.log',filemode='w', format="%(asctime)s - %(message)s")

logging.debug('debug')

class Gateway(LLMbase):
    def __init__(self,*, Config: Config,llm_provider:LLMbase) -> None:

        self.llm_provider = llm_provider
        self.sleep = time.sleep
        self.max_attempts = Config.max_attempts
        self.base_delay = Config.base_delay
        self.random_unform = random.uniform


    def chat(self,*,chat_input:Chat):
        for attempts in range(1,self.max_attempts+1):
            try:
                return self.llm_provider.chat(chat_input=chat_input)
            except(Connection_Error,RateLimit_Error,Provider_Error,Authentication_Error) as e:
               if attempts == self.max_attempts:
                   logging.error("llm_retry_exhausted attempts=%s", attempts)
                   raise 
               celling = self.base_delay * (2**(attempts-1))
               delay = self.random_unform(0,celling)
               logging
               self.sleep(delay)
               
             