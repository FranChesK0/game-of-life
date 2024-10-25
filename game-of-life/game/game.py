import copy
import random
from typing import List, Tuple, Optional

from core import logger
from utils import SingletonMeta


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width: int = 20, height: int = 20) -> None:
        self.__width = width
        self.__height = height
        self.__life_count = 0

        self.__world: List[List[bool]] = []
        self.generate_world()
        self.__prev_world = copy.deepcopy(self.world)

    def __repr__(self) -> str:
        return (
            f"GameOfLife<{id(self)}>["
            f"width:{self.__width}, "
            f"height:{self.__height}, "
            f"life_count:{self.__life_count}"
            "]"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def world(self) -> List[List[bool]]:
        return self.__world

    @property
    def previous_world(self) -> List[List[bool]]:
        return self.__prev_world

    @property
    def life_count(self) -> int:
        return self.__life_count

    def generate_world(self) -> None:
        self.__world = [
            [bool(random.randint(0, 1)) for _ in range(self.__width)]
            for _ in range(self.__height)
        ]
        logger.debug(f"world generated: {self}")

    def form_new_generation(self) -> None:
        self.__life_count += 1
        if self.life_count <= 0:
            return

        new_world = [[False for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                near = self.__get_near(self.world, (i, j))

                if self.world[i][j]:
                    if near not in (2, 3):
                        new_world[i][j] = False
                    else:
                        new_world[i][j] = True
                    continue
                if near == 3:
                    new_world[i][j] = True
                else:
                    new_world[i][j] = False

        self.__prev_world = copy.deepcopy(self.world)
        self.__world = new_world
        logger.debug(f"world updated: {self}")

    @staticmethod
    def __get_near(
        world: List[List[bool]],
        pos: Tuple[int, int],
        system: Optional[Tuple[Tuple[int, int], ...]] = None,
    ) -> int:
        if system is None:
            system = (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            )

        count = 0
        for i in system:
            if world[(pos[0] + i[0]) % len(world)][(pos[1] + i[1]) % len(world[0])]:
                count += 1
        return count
