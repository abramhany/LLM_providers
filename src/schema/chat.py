from pydantic import BaseModel , Field  
from typing import Type
from enums.roles import Role
from .ticket import Ticket


class Message(BaseModel):
    role : Role
    content : str


class Chat(BaseModel):

    messages : list[Message] = Field(default_factory=list)

    temperature : float = Field(default=1.0,ge=0.0)

    top_p : float | None = Field(default=None,ge=0.0,le=1.0)

    top_k: int | None = Field(default=None,ge=1)

    max_new_tokens: int = Field(default=100,ge=1)

    text_format : Type[BaseModel] | None = None