import os
import logging
from logging import config as setup_logger_config

from core import config

from .logger_config import logger_config, logs_directory

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

setup_logger_config.dictConfig(logger_config)
logger = logging.getLogger("debug" if config.debug else "main")
