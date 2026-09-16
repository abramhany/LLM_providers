from pydantic_settings import BaseSettings , SettingsConfigDict
from pydantic import Field

class Config(BaseSettings):

    groq_api_key : str = Field(min_length=1,validation_alias='GROQ_API_KEY')
    base_url :str = Field('https://api.groq.com/openai/v1',min_length=1,validation_alias='BASE_URL')
    model_name : str = Field(min_length=1,validation_alias='MODEL_NAME')
    timeout : float = Field(ge=0,validation_alias="TIME_OUT")


    model_config = SettingsConfigDict(env_file='.env',env_file_encoding="utf-8",
        extra="ignore",protected_namespaces=())