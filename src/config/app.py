from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    HOST: str
    PORT: int
    TZ: str
    # For Debug
    DEBUG_PORT: int
    DEBUG: bool

app = AppSettings()
