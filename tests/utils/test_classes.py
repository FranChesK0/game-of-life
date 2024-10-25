import threading
from typing import List

import pytest  # noqa: F401

from utils import SingletonMeta


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value: int = 0) -> None:
        self.value = value


class TestSingletonMeta:
    def test_singleton_instance(self) -> None:
        """
        Test that multiple instances of a singleton class return the same object.
        """
        instance1 = SingletonClass(10)
        instance2 = SingletonClass()

        # Assert that both instances are the same
        assert instance1 is instance2, "SingletonMeta did not return the same instance"

        # Ensure the value has not changed after the second instantiation
        assert (
            instance1.value == 10
        ), "SingletonMeta instance value should not change after re-instantiation"

    def test_singleton_initialization_arguemnts(self) -> None:
        """
        Test that singleton class creates new instances with subsequent
        instantiation arguments.
        """
        instance1 = SingletonClass(10)
        instance2 = SingletonClass(20)
        instance3 = SingletonClass()

        # Assert that instances are different
        assert instance1 is not instance2, (
            "SingletonMeta did not changed"
            "after re-instantiation with subsequent arguments"
        )
        # Assert that instances are the same
        assert instance2 is instance3, "SingletonMeta did not return the same instance"

        # Ensure the value has changed after the second re-instantiation
        assert instance3.value == 20, (
            "SingletonMeta instance value should change"
            "after re-instantiation with subsequent arguments"
        )

    def test_thread_safety(self) -> None:
        """
        Test that SingletonMeta is thread-safe by creating multiple instances
        from different threads and ensuring they all return the same object.
        """
        # List to hold instances created by threads
        instances: List[SingletonClass] = []

        def create_instance() -> None:
            instances.append(SingletonClass())

        # Create multiple threads
        threads = [threading.Thread(target=create_instance) for _ in range(10)]

        # Start all threads
        for thread in threads:
            thread.start()

        # Ensure all threads have completed
        for thread in threads:
            thread.join()

        # Ensure all instances are the same object
        assert all(
            instance is instances[0] for instance in instances
        ), "SingletonMeta is not thread-safe"
