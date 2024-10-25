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
