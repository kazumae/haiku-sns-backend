from typing import Union

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DATABASE_URL: str
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    SMTP_HOST: str
    SMTP_PORT: int
    # CORSの設定
    CORS_ORIGINS: list[str] = Field(
        default=["http://localhost:3000", "http://127.0.0.1:3000"]
    )

    @field_validator("CORS_ORIGINS", mode="before")
    def split_cors_origins(cls, v: Union[str, list[str]]) -> list[str]:
        if isinstance(v, str) and "," in v:
            return [origin.strip() for origin in v.split(",")]
        elif isinstance(v, str):
            return [v.strip()]
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = AppSettings()
