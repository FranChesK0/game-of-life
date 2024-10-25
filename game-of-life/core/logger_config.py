"""
Logger Configuration for Game of Life Application

This module defines the logging configuration for the Game of Life application. It
specifies how logs are formatted, where they are directed, and the logging behavior
for different components of the application. The configuration supports logging to
both console and file outputs, with customizable log levels and formats.

Attributes:
-----------
root_directory: str
    The root directory of the project, determined based on the location of this file.
logs_directory: str
    The directory where log files are stored. This is created under the project
    root directory.
logger_config: dict
    A dictionary defining the logging configuration using Python's `logging` module.
    It includes the following components:

    - `version`: The version of the logging configuration schema.
    - `formatters`: Specifies different log messages formats for console and file
        handlers.
        - `console`: A simple format for console logs showing log level, module,
            filename, line number, and message.
        - `file`: A more detailed format for file logs including timestamp, log
            level, module, filename, line number, and message.
    - `handlers`: Defines handlers that determine where logs are sent.
        - `console`: A `StreamHandler` that outputs logs to the console, set to
            handle `DEBUG` level logs and above.
        - `log_file`: A `FileHandler` that writes logs to a file named
            "game-of-life.log" located in the `logs_directory`, set to handle `ERROR`
            level logs and above.
    - `loggers`: Specifies different loggers for the application.
        - `""` (root logger): Handles all logs not explicitly managed by other
            loggers, with console output enabled.
        - `debug`: A logger used for detailed debugging, outputs to the console,
            and does not propagate logs to the root logger.
        - `main`: The primary logger for general application use, configured to
            send logs to both the console and file, handling `INFO` level logs and
            above.

Usage:
------
This configuration can be loaded using Python's `logging.config.dictConfig()` to
initialize the logging system:

```python
import logging.config

from core.logger_config import logger_config

logging.config.dictConfig(logger_config)
logger = logger.getLogger("main")
logger.info("Game of Life application has started...")
```

Notes:
------
- The log file ("game-of-life.log") will be created in the `logs` directory under the
    project root. Ensure that the directory exists or is created at runtime.
- Adjust the log levels and handlers as needed for different environments
    (e.g., development, production).
"""

import os

root_directory = os.path.dirname(os.path.abspath(__file__)).removesuffix(
    os.path.join("game-of-life", "core")
)
logs_directory = os.path.join(root_directory, "logs")

logger_config = {
    "version": 1,
    "formatters": {
        "console": {
            "format": "%(levelname)s - %(module)s:%(filename)s:%(lineno)s - %(message)s"
        },
        "file": {
            "format": (
                "%(asctime)s - %(levelname)s - "
                "%(module)s:%(filename)s:%(lineno)s - %(message)s"
            )
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "console",
        },
        "log_file": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "file",
            "filename": os.path.join(logs_directory, "game-of-life.log"),
            "mode": "a",
        },
    },
    "loggers": {
        "": {"level": "NOTSET", "handlers": ["console"]},
        "debug": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "main": {
            "level": "INFO",
            "handlers": ["console", "log_file"],
            "propagate": False,
        },
    },
}
