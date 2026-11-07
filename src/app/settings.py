from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class App(BaseModel):
    s3_key: str = "your_key" 
    google_api_key: str = "your_google_key"
    
    model_config = SettingsConfigDict(env_prefix="APP_")


class Settings(BaseSettings):
    app: App = Field(default_factory=App)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="_",
        env_nested_max_split=1,
    )

settings = Settings()