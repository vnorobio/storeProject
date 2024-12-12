from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Required PostgreSQL configuration
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password123"
    POSTGRES_DB: str = "store_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # Generate the full PostgreSQL connection URL
    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        # Enable loading environment variables from a `.env` file
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate settings for use across your app
settings = Settings()
