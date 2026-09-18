from config.config import Config
import random

from schema.ticket import Ticket
from .base import LLMbase
from exceptions.exceptions import Connection_Error,RateLimit_Error  , Provider_Error , Authentication_Error , LLMErrorException
from schema.chat import Chat
from enums.llm_error import LLMError
import time
import logging

logging.basicConfig(level=logging.DEBUG, filename='info.log',filemode='w', format="%(asctime)s [%(levelname)s] (%(name)s): %(message)s",datefmt="%H:%M:%S",)
logger = logging.getLogger(__name__)
logging.debug('debug')

class Gateway(LLMbase):
    def __init__(self,*, Config: Config,llm_provider:LLMbase) -> None:

        self.llm_provider = llm_provider
        self.sleep = time.sleep
        self.max_attempts = Config.max_attempts
        self.base_delay = Config.base_delay
        self.random_unform = random.uniform


    def generation(self,*,chat_input:Chat):
        for attempts in range(1,self.max_attempts+1):
            try:
                logger.info("attempting to send request to the llm")
                return self.llm_provider.generation(chat_input=chat_input)
            except(Connection_Error,RateLimit_Error,Provider_Error,Authentication_Error) as e:
               if attempts == self.max_attempts:
                   logging.info("llm_retry_exhausted attempts=%s", attempts)
                   raise
               celling = self.base_delay * (2**(attempts-1))
               delay = self.random_unform(0,celling)
               logging.info('time of delay is delay=%s',delay)
               self.sleep(delay)
            except LLMErrorException as e:
                logging.error(e)
                raise e
            
    def structured_generation(self,*,chat_input:Chat):
            for attempts in range(1,self.max_attempts+1):
                try:
                    logger.info("attempting to send request to the llm")
                    return self.llm_provider.structured_generation(chat_input=chat_input)
                except(Connection_Error,RateLimit_Error,Provider_Error,Authentication_Error) as e:
                   if attempts == self.max_attempts:
                       logging.info("llm_retry_exhausted attempts=%s", attempts)
                       raise
                   celling = self.base_delay * (2**(attempts-1))
                   delay = self.random_unform(0,celling)
                   logging.info('time of delay is delay=%s',delay)
                   self.sleep(delay)
                except LLMErrorException as e:
                    logging.error(e)
                    raise e
    
        