from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'ticket'
    # database_url: str
    # app_author: str
    # db_url: str = 'sqlite://login:password@127.0.0.1:5432/ticket'
    # path: str

    class Config:
        env_file = '.env' 


settings = Settings() 