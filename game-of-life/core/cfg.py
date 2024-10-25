import os
import sys
from typing import Optional

from pydantic_settings import BaseSettings

from core import logger


def _load_port() -> Optional[int]:
    port = os.getenv("GAME_OF_LIFE_PORT")
    if port is None:
        logger.warning("'GAME_OF_LIFE_PORT' is not set")
        return port
    try:
        return int(port)
    except ValueError:
        logger.error("could not parse 'GAME_OF_LIFE_PORT'")
        return None


def _load_addr() -> Optional[str]:
    addr = os.getenv("GAME_OF_LIFE_ADDR")
    if addr is None:
        logger.warning("'GAME_OF_LIFE_ADDR' is not set")
    return addr


class Config(BaseSettings):
    debug: bool = "-d" in sys.argv or "--debug" in sys.argv
    addr: str = _load_addr() or "0.0.0.0"
    port: int = _load_port() or 3000


config = Config()
