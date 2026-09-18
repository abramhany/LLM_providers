import logging 
from providers.openai_gateway import OpenAIGateway
from providers.gateway import Gateway
from config.config import Config
from schema import Chat , Message , Ticket
from enums.roles import Role
from prompt.summarizer import summary_prompt



logger = logging.getLogger(__name__)


settings = Config()

sum_prompt = summary_prompt()


message_list =[ Message(role=Role.SYSTEM,content=sum_prompt),Message(role=Role.USER,content='My laptop broke and i cant do my home work')]

gateway = Gateway(Config=settings,llm_provider=OpenAIGateway(config=settings))




chat = Chat(messages=message_list,text_format=Ticket)
response = gateway.structured_generation(chat_input=chat)



print(response)
print(type(response))
