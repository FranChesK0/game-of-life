import pytest

from utils import SingletonMeta


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, field: str = "test string") -> None:
        self.field = field


class TestSingletonMeta:
    @pytest.mark.parametrize(
        "instance_1, instance_2",
        [
            (SingletonClass(), SingletonClass()),
            (SingletonClass("test string 1"), SingletonClass()),
        ],
    )
    def test_one_instance(
        self,
        instance_1: SingletonClass,
        instance_2: SingletonClass,
    ) -> None:
        assert instance_1.field == instance_2.field
        assert id(instance_1) == id(instance_2)

    @pytest.mark.parametrize(
        "instance_1, instance_2",
        [
            (SingletonClass(), SingletonClass("test string 2")),
            (SingletonClass("test string 3"), SingletonClass("test string 4")),
        ],
    )
    def test_multiple_instances(
        self,
        instance_1: SingletonClass,
        instance_2: SingletonClass,
    ) -> None:
        assert instance_1.field != instance_2.field
        assert id(instance_1) != id(instance_2)
