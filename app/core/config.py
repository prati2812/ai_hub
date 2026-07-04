from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    app_name:str
    app_version:str
    debug: bool
    gemini_api_key: str
    database_url: str
    jwt_secret: str

    class Config:
        env_file = ".env"

settings = Settings()
