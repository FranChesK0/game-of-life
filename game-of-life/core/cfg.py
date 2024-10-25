"""
Configuration Management for Game of Life Application

This module handles the configuration settings for the Game of Life application.
It leverages environment variables, command-line arguments, and default values
to set up application-specific settings such as the address, port, and debug mode.
The configuration is managed using Pydantic's `BaseSettings` for easy integration
and validation.

Functions:
----------
_load_port() -> Optional[int]:
    Attempts to load the port number from the `GAME_OF_LIFE_PORT` environment variable.
    If the variable is not set, a warning is logged, and `None` is returned.
    If the variable is set but cannot be converted to an integer, an error is logged,
    and `None` is returned.

_load_addr() -> Optional[str]:
    Attempts to load the address from the `GAME_OF_LIFE_ADDR` environment variable.
    If the variable is not set, a warning is logged, and the function returns `None`.

Classes:
--------
Config(BaseSettings):
    A Pydantic settings class that manages the application's configuration. It reads
    from environment variables and command-line arguments, providing a centralized
    place for application settings.

    Attributes:
    -----------
    - `debug` (bool): Indicates whether the application is running in debug mode.
        This is determined by the presence of `-d` or `--debug` in the command-line
        arguments.
    - `addr` (str): The address the application will bind to. Defaults to "0.0.0.0"
        if `GAME_OF_LIFE_ADDR` is not set.
    - `port` (int): The port the application will listen on. Defaults to `3000` if
        `GAME_OF_LIFE_PORT` is not set or cannot be parsed.

Attributes:
-----------
config: Config
    An instance of the `Config` class that holds the current configuration settings
    for the application.


Usage:
------
This module can be imported to access the configuration settings throughout the
application:

```python
from core.cfg import config

print(f"Starting server on {config.addr}:{config.port}")
if config.debug:
    print("Debug mode is enabled")
```

Notes:
------
- Ensure that environment variable `GAME_OF_LIFE_ADDRESS` and `GAME_OF_LIFE_PORT`
    are set correctly if you want to override the default values.
- Command-line arguments `-d` or `--debug` will enable debug mode, which can be
    useful for development and troubleshooting.
"""

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
        logger.error(f"could not parse 'GAME_OF_LIFE_PORT': {port}")
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
