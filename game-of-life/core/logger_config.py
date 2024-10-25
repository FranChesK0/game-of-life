import os

root_directory = os.path.dirname(os.path.abspath(__file__)).removesuffix(
    os.path.join("game-of-life", "core")
)

logger_config = {
    "version": "0.1.0",
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
            "filename": os.path.join(root_directory, "logs", "game-of-life.log"),
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
