import os
from pydantic import BaseSettings


class CURDBOYSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


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