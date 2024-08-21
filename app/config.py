# app/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SNOWFLAKE_USER: str
    SNOWFLAKE_PASSWORD: str
    SNOWFLAKE_ACCOUNT: str
    SNOWFLAKE_WAREHOUSE: str
    SNOWFLAKE_DATABASE: str
    SNOWFLAKE_SCHEMA: str
    SNOWFLAKE_ROLE: str

    class Config:
        env_file = ".env"


settings = Settings()
