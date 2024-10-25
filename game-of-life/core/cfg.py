import os
import sys
from typing import Optional

from pydantic_settings import BaseSettings


def load_port() -> Optional[int]:
    port = os.getenv("GAME_OF_LIFE_PORT")
    if port is None:
        return port
    try:
        return int(port)
    except ValueError:
        return None


class Config(BaseSettings):
    debug: bool = "-d" in sys.argv or "--debug" in sys.argv
    addr: str = os.getenv("GAME_OF_LIFE_ADDR") or "0.0.0.0"
    port: int = load_port() or 3000


config = Config()
