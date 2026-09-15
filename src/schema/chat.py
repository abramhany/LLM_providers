from pydantic import BaseModel , Field 
from typing import Literal


class Chat(BaseModel):
    role : Literal['user','system']
    message : str = Field(min_length=1)
