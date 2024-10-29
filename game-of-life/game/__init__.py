"""
Game of Life Implementation

This module contains the `GameOfLife` class that implements Conway's Game of Life,
a cellular automation devised by mathematician John Horton Conway. The game is played
on a grid where each cell can be either alive (True) or dead (False). The next state
of the gird is determined by the current state and the number of alive neighbors each
cell has.

Classes:
--------
GameOfLife(metaclass=SingletonMeta):
    A singleton class that manages the state and behavior of the Game of Life.
    It initializes the game world, generates new generations, and maintains
    the current and previous states of the grid.

    Attributes:
    -----------
    __width: int
        The width of the game world grid.
    __height: int
        The height of the game world grid.
    __velocity: float
        The velocity of the world generation in seconds.
    __life_count: int
        The number of generations that have been created.
    __world: List[List[bool]]
        The current state of the game world (grid).
    __prev_world: List[List[bool]]
        A deep copy of the previous sate of the game world.

    Properties:
    -----------
        velocity: float
            The velocity of the world generation in seconds.
        world: List[List[bool]]
            The current game world grid.
        previous_world: List[List[bool]]
            The previous game world grid.
        life_count: int
            The number of generations that have occurred.

    Methods:
    --------
        __init__(width: int = 20, height: int = 20) -> None:
            Initializes a new Game of Life instance with the specific width and height,
            generating and initial random world.
        __repr__() -> str:
            Returns a string representation of the GameOfLife instance, including its
            width, height, and life count.
        __str__() -> str:
            Returns a string representation of the GameOfLife instance.
        generate_world() -> None:
            Generates a new random world (grid) for the game, populating it with
            randomly assigned alive and dead cells.
        form_new_generation() -> None:
            Advances the game to the next generation based on the rules of Conway's Game
            of Life. Updates the current world and keeps track of the previous world.
        __get_near(
            world: List[List[bool]],
            pos: Tuple[int, int],
            system: Optional[Tuple[Tuple[int, int], ...]] = None,
        ) -> int:
            A static method that counts the number of alive neighbors around a specific
            cell position in the game world. Uses toroidal (wrap-around) boundary
            conditions.

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

from .game import GameOfLife

__all__ = ["GameOfLife"]
