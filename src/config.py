from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "DirectCase"
    app_version: str = "0.1.0"
    admin_email: str = "diegorosariosousa@gmail.com"
    debug: bool = False


class DebugSettings(Settings):
    debug: bool = True
