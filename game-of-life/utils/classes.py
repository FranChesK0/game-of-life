from typing import Any, Dict
from threading import Lock


class SingletonMeta(type):
    _instance: Dict[type["SingletonMeta"], "SingletonMeta"] = {}
    _lock: Lock = Lock()

    @classmethod
    def __call__(cls, *args: Any, **kwds: Any) -> "SingletonMeta":
        with cls._lock:
            if cls not in cls._instance or args or kwds:
                instance = super().__call__(*args, **kwds)
                cls._instance[cls] = instance
        return cls._instance[cls]
