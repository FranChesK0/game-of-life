from typing import Any, Dict
from threading import Lock


class SingletonMeta(type):
    _instance: Dict["SingletonMeta", "SingletonMeta"] = {}
    _lock: Lock = Lock()

    def __call__(self, *args: Any, **kwds: Any) -> "SingletonMeta":
        with self._lock:
            if self not in self._instance or args or kwds:
                instance = super().__call__(*args, **kwds)
                self._instance[self] = instance
        return self._instance[self]
