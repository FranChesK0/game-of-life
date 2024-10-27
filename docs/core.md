# Core Module for Game of Life Application

This module is responsible for configuration the essential settings and logging functionality required by the Game of Life application. It consists of components that handle configuration management, logging setup, and environmental variable handling, providing a unified interface for application-wide settings.

## Modules
- `core/logger_config.py`: Defines the logging configuration, including formatters, handlers, and loggers for console and file outputs.
- `core/logger_setup.py`: Sets up the logger based on the configuration defined in `logger_config.py`, ensuring logs are properly routed to console or file based on the application's runtime arguments.
- `core/cfg.py`: Manages the application's configuration settings, including reading from environment variables, command-line arguments, and default values using Pydantic's `BaseSettings`.
- `core/__init__.py`: Initializes and exposes the `config` and `logger` for use throughout the application.

## Usage
Import the `config` and `logger` from the `core` module to utilize logging and configuration in other parts of the application:
```python
from core import config, logger

logger.info("Starting the Game of Life application...")
address = config.addr
port = config.port
secret = config.secret
```

## Modules Details
1. `core/logger_config.py`:
    - Defines a dictionary `logger_config` that specifies the logging behavior.
    - Supports different formats for console and file outputs, and separates handlers for debug and main logging.
    - Create a directory for log files (`logs`) under the root directory.
2. `core/logger_setup.py`:
    - Sets up logger using Python's `logging` module and the configuration from `logger_config.py`.
    - Determines whether to run in debug mode based on command-line arguments (`-d` or `--debug`).
    - Creates the `logs` directory if it doesn't exist.
3. `core/cfg.py`:
    - Manages configuration using Pydantic's `BaseSettings`.
    - Reads configuration values `addr`, `port` and `secret` from environment variables (`GAME_OF_LIFE_ADDR`, `GAME_OF_LIFE_PORT`, `GAME_OF_LIFE_SECRET`).
    - Falls back to default values if environment variables are not set or are invalid.
    - Logs warnings or errors if there are issues loading the configuration.
4. `core/__init__.py`:
    - Imports and exposes `config` and `logger` for external usage.
    - Ensures that other modules can easily access centralized configuration and logging functionality.

## Logging
The logging setup is configurable to handle different levels of verbosity. Console logs are primarily used for debugging, while file logs capture errors. Adjustments can be made to the logging behavior by modifying `core/logger_config.py`.

## Configuration
The configuration can be customized via environment variables:
- Command-line arguments `-d` or `--debug` can be used to enable debug logging.
- `GAME_OF_LIFE_ADDR`: Sets the address for the application (default: "0.0.0.0").
- `GAME_OF_LIFE_PORT`: Sets the port number for the application (default: 3000).
- `GAME_OF_LIFE_SECRET`: Sets the secret key for the application (default: auto generated string)
