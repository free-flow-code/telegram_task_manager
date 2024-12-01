from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore"
    )
    BOT_TOKEN: str
    DB_FILENAME: str = "mydb.sqlite3"
    SERVER_TZ: str = "Europe/Moscow"


settings = Settings()
