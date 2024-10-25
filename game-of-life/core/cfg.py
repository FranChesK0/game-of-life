import os
import sys

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    debug: bool = "-d" in sys.argv or "--debug" in sys.argv
    addr: str = os.getenv("GAME_OF_LIFE_ADDR") or "0.0.0.0"
    port: str = os.getenv("GAME_OF_LIFE_PORT") or "3000"


config = Config()
