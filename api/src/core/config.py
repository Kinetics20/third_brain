from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., alias="OPENAI_API_KEY")


settings = Settings()
