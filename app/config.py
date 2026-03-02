from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SERVICE_URL : str = "http://127.0.0.1:8000"
    POST_SERVICE_URL : str = "http://127.0.0.1:8080"
    class Config:
        env_file = f".env.local"
        
settings = Settings()