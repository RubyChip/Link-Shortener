from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    PROJECT_NAME: str = "Link shortener"
    API_V1: str = "/api/v1"
    URL_DOMAIN: str = "http://mysite.com/"

    DATABASE_LOGS: bool = False

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: str = "5432"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_NAME: str = "postgres"

    UNIQUE_CODE_LENGTH: int = 5

    class Config:
        env_file = "env/.env.example"
        env_file_encoding = "utf-8"


settings = Settings()
