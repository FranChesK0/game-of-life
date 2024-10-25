"""
Logger Setup for Game of Life Application

This module sets up the logging system for the Game of Life application base on the
configuration defined in `logger_config`. It ensures that logs are properly routed
to console or file outputs, depending on the application's runtime settings and
command-line arguments.

Functionality:
--------------
1. Directory Creation:
    - Checks if the `logs` directory (specified by `logs_directory`) exists.
    - Creates the directory if it does not exist, ensuring that log files can be
        written without issues.

2. Logging Configuration:
    - Loads the logging configuration from `logger_config` using
        `logging.config.dictConfig()`.
    - Sets up a logger instance that operates in either "debug" or "main" mode
        base on command-line arguments.
        - `debug` mode is activated when the application is run with `-d` or `--debug`
            arguments, enabling more verbose logging for development and troubleshooting.
        - `main` mode is the default, providing standard logging behavior for production
            use.

Attributes:
-----------
logger: logging.Logger
    The logger instance configured to handle logs for the application. It switches
    between "debug" and "main" loggers based on command-line arguments.

Usage:
------
This module can be imported to set up logging across the application:

```python
from core.logger_setup import logger

logger.info("Application started in standard mode.")
logger.debug("This is a debug message, visible only in debug mode.")
```

Notes:
------
- Ensure that the `logs` directory has appropriate permissions for writing logs files.
- Adjust the logging behavior by modifying `logger_config` in `core/logger_config.py`.
- Command-line flags `-d` or `--debug` will trigger more verbose logging, useful during
    development.
"""

import os
import sys
import logging
from logging import config

from .logger_config import logger_config, logs_directory

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

config.dictConfig(logger_config)
logger = logging.getLogger(
    "debug" if "-d" in sys.argv or "--debug" in sys.argv else "main"
)
