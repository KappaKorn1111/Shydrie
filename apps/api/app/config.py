from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Shydrie API"
    api_version: str = "0.1.0"
    postgres_dsn: str = "postgresql://postgres:postgres@localhost:5432/shydrie"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "changeme"
    minio_endpoint: str = "localhost:9000"
    minio_access_key: str = "minioadmin"
    minio_secret_key: str = "minioadmin"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
