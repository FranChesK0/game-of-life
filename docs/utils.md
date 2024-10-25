# Utility Classes for Game of Life Application

This module provides utility classes and patterns that can be used across the
Game of Life application. It currently includes an implementation of the Singleton
design pattern to ensure that a class has only one instance, even when instantiated
multiple times.

## Modules
- `utils/classes.py`: Defines the `SingletonMeta` metaclass, which can be used to
    create singleton classes.

## Classes
SingletonMeta (metaclass):
    A metaclass that implements the Singleton pattern. It ensures that only one
    instance of a class is created, regardless of how many times the class is
    instantiated. Thread-safe implementation using a lock to prevent race conditions
    during instantiation.

## Attributes
_instance: Dict[SingletonMeta, SingletonMeta]
    A dictionary that stores the single instance of each class that uses
    `SingletonMeta` as its metaclass.
_lock: Lock
    A threading lock that ensures thread-safe instantiation of singleton classes.

## Usage
To use `SingletonMeta`, declare it as the metaclass of a class you want to implement
as a singleton:

```python
from utils import SingletonMeta


class MySingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42


# Both of these will return the instance
singleton1 = MySingletonClass()
singleton2 = MySingletonClass()
assert singleton1 is singleton2
```

## Notes
- The `SingletonMeta` ensures that the class is thread-safe, meaning that even in
    multi-threaded environments, only one instance will be created.
- The singleton instance is stored in a dictionary, and re-instantiation with different
    arguments will not override the existing instance.
