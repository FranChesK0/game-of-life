import copy
import random
from typing import List, Tuple, Optional

from core import logger
from utils import SingletonMeta


class GameOfLife(metaclass=SingletonMeta):
    """
    A singleton class that manages the state and behavior of the Game of Life.
    It initializes the game world, generates new generations, and maintains
    the current and previous states of the grid.

    Attributes:
    -----------
    __width: int
        The width of the game world grid.
    __height: int
        The height of the game world grid.
    __life_count: int
        The number of generations that have been created.
    __world: List[List[bool]]
        The current state of the game world (grid).
    __prev_world: List[List[bool]]
        A deep copy of the previous sate of the game world.

    Properties:
    -----------
        world: List[List[bool]]
            The current game world grid.
        previous_world: List[List[bool]]
            The previous game world grid.
        life_count: int
            The number of generations that have occurred.

    Usage:
    ------
    To create and run the Game of Life, instantiate the `GameOfLife` class and call
    `form_new_generation()` to advance the game. For example:

    ```python
    game = GameOfLife()
    game.form_new_generation()
    print(game.world)
    ```
    """

    def __init__(self, width: int = 20, height: int = 20) -> None:
        """
        Initializes a new Game of Life instance with the specific width and height,
        generating and initial random world.

        Parameters:
        -----------
            width: int
                The width of the game world grid (Default: 20).
            height: int
                The height of the game world grid (Default: 20).
        """
        self.__width = width
        self.__height = height
        self.__life_count = 0

        self.__world: List[List[bool]] = []
        self.generate_world()
        self.__prev_world = copy.deepcopy(self.world)

    def __repr__(self) -> str:
        """
        Returns a string representation of the GameOfLife instance, including its
        width, height, and life count.
        """
        return (
            f"GameOfLife<{id(self)}>["
            f"width:{self.__width}, "
            f"height:{self.__height}, "
            f"life_count:{self.__life_count}"
            "]"
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the GameOfLife instance.
        """
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
        """
        Generates a new random world (grid) for the game, populating it with
        randomly assigned alive and dead cells.
        """
        self.__world = [
            [bool(random.randint(0, 1)) for _ in range(self.__width)]
            for _ in range(self.__height)
        ]
        logger.debug(f"world generated: {self}")

    def form_new_generation(self) -> None:
        """
        Advances the game to the next generation based on the rules of Conway's Game
        of Life. Updates the current world and keeps track of the previous world.
        """
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
        """
        A static method that counts the number of alive neighbors around a specific
        cell position in the game world. Uses toroidal (wrap-around) boundary
        conditions.

        Parameters:
        -----------
            world: List[List[bool]]
                The game world grid.
            pos: Tuple[int, int]
                A specific cell position to check around.
            system: Optional[Tuple[Tuple[int, int], ...]] = None
                Check conditions.
        """
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
