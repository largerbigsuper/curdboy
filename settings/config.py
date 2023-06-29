import os
from typing import List
from pydantic import BaseSettings

class CURDBOYSettings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    APP_OPENAPI_URL: str = "/docs"
    APP_ALLOW_ORIGINS: List[str] = ["http://localhost", "http://localhost:8000"]
    APP_ALLOW_METHODS: List[str] = ["get", "post", "update", "delete"]
    

class ProdSettings(CURDBOYSettings):

    class Config:
        case_sensitive = True
        env_file = "settings/prod.env"
        env_file_encoding = 'utf-8'



class TestSettings(CURDBOYSettings):

    class Config:
        case_sensitive = True
        env_file = "settings/test.env"
        env_file_encoding = 'utf-8'


class DevSettings(CURDBOYSettings):

    class Config:
        case_sensitive = True
        env_file = "settings/dev.env"
        env_file_encoding = 'utf-8'


settings = None
env = os.getenv('CURDBOY_ENV', 'dev').lower()
if env == 'prod':
    settings = ProdSettings()
elif env == 'test':
    settings = TestSettings()
elif env == 'dev':
    settings = DevSettings()