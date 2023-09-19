from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from src.core.enums import EnvEnum

load_dotenv()


class Settings(BaseSettings):
    ENV: EnvEnum = EnvEnum.LOCAL
    VERSION: str = "0.0.1"
    BASE_DIR: str = str(Path(__file__).resolve().parent.parent.parent)

    API_KEY: str = ""

    model_config = SettingsConfigDict(env_prefix="CONF_")

    @property
    def DEBUG(self) -> bool:
        return self.ENV in ["local", "dev"]
