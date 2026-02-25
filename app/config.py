from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SERVICE_URL : str = "http://127.0.0.1:8000"
    class Config:
        env_file = f".env.local"
        
settings = Settings()