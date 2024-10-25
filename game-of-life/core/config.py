import os
import sys

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = "-d" in sys.argv or "--debug" in sys.argv
    ADDRESS: str = os.getenv("GAME_OF_LIFE_ADDR") or "0.0.0.0"
    PORT: str = os.getenv("GAME_OF_LIFE_PORT") or "3000"


CONFIG = Config()
