from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str
    CONTROLLER_APP: str  # fastapi, django, flask, cli
    CONTROLLER_HOST: str  # 0.0.0.0
    CONTROLLER_PORT: int  # 9000
    REPOSITORY: str  # pgsqlalchemy, dynamodb, filesystem, memory
    CORS_ORIGINS: str  # "http://127.0.0.1,http://127.0.0.1:3000"
    API_URL_PREFIX: str
    API_APP: str

    DEBUG_HOST: str
    DEBUG_PORT: int  # 5678

    # class Config:
    #     case_sensitive = True
