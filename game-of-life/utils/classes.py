from typing import Any, Dict
from threading import Lock


class SingletonMeta(type):
    """
    SingletonMeta Metaclass

    A thread-safe implementation of the Singleton design pattern. This metaclass ensures
    that only one instance of a class is created, even if multiple instantiations are
    attempted. Classes that use `SingletonMeta` as their metaclass will behave as
    singletons, sharing the same instance across the application.

    Attributes:
    -----------
    _instance: Dict[SingletonMeta, SingletonMeta]
        A dictionary that stores the single instance of each class that uses
        `SingletonMeta` as its metaclass. The key is the metaclass, and the
        value is the instance of the class.
    _lock: Lock
        A threading lock that ensures thread-safe access to the singleton instance.
        This prevents race conditions during the creation of the singleton instance
        in multi-threading environments.

    Methods:
    --------
    __call__(*args: Any, **kwds: Any) -> SingletonMeta
        Overrides the `__call__` method to control the instantiation of the class.
        It checks if an instance already exists; if not, creates a new one. The
        method is thread-safe to ensure only one instance is created, even in
        multi-threaded contexts.

    Usage:
    ------
    To create a singleton class, use `SingletonMeta` as the metaclass:

    ```python
    class MySingletonClass(metaclass=SingletonMeta):
        def __init__(self):
            self.value = 42


    # Both of these will return the same instance
    singleton1 = MySingletonClass()
    singleton2 = MySingletonClass()
    assert singleton1 is singleton2
    ```

    Notes:
    ------
    - If the class is instantiated with arguments (`args` or `kwds`) and the instance
        does not yet exist, those arguments will be used for the initial creation.
    - Subsequent instantiations with different arguments will not recreate the instance,
        meaning the singleton retains the first set of arguments it was initialized with.
    - The implementation is thread-safe, ensuring a consistent singleton instance across
        multiple threads.
    """

    _instance: Dict["SingletonMeta", "SingletonMeta"] = {}
    _lock: Lock = Lock()

    def __call__(self, *args: Any, **kwds: Any) -> "SingletonMeta":
        with self._lock:
            if self not in self._instance or args or kwds:
                instance = super().__call__(*args, **kwds)
                self._instance[self] = instance
        return self._instance[self]
