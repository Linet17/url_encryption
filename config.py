from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    BASE_URL: str
    DB_URL: str
    CONTACT_NAME: str
    CONTACT_EMAIL: str

    class Config:
        env_file = ".env"

settings = Settings()