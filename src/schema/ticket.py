from pydantic import BaseModel
from typing import Literal



class Ticket(BaseModel):
    
    category: Literal['technical','account','delivery',"billing",'subscription']
    sentiment: Literal['negative','neutral','positive']
    urgency: Literal['high','medium','low']
    summary : str
