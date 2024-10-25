import os
import logging
from logging import config

from core import CONFIG

from .logger_config import logger_config, logs_directory

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

config.dictConfig(logger_config)
logger = logging.getLogger("debug" if CONFIG.DEBUG else "main")
