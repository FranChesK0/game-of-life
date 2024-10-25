import pytest  # noqa: F401

from game import GameOfLife


class TestGameOfLife:
    def test_initialization(self) -> None:
        """
        Test that the GameOfLife initializes with default width and height.
        """
        game = GameOfLife()
        assert game.world is not None, "Initial world should not be None"
        assert len(game.world) == 20, "Initial world height should be 20"
        assert len(game.world[0]) == 20, "Initial world width should be 20"
        assert game.life_count == 0, "Initial life count should be 0"

    def test_world_generation(self) -> None:
        """
        Test that the generate_world method populates the world correctly.
        """
        game = GameOfLife()
        initial_world = game.world

        # Generate a new world
        game.generate_world()
        new_world = game.world

        assert initial_world != new_world, "World should be different after generation"

    def test_form_new_generation(self) -> None:
        """
        Test that form_new_generation update the world correctly.
        """
        game = GameOfLife(4, 4)

        # Set up a simple world with known state
        game._GameOfLife__world = [  # type: ignore[attr-defined]
            [False, True, False, True],
            [True, True, True, False],
            [False, True, False, False],
            [True, True, False, True],
        ]

        # Initially, the life count should be 0
        assert game.life_count == 0, "Initial life count should be 0"

        # Advance to the next generation
        game.form_new_generation()
        assert game.life_count == 1, "Life count should increase after generation"

        # Expected next state based on the rules of the Game of Life
        expected_next_world = [
            [False, False, False, False],
            [False, False, False, True],
            [False, False, False, False],
            [False, True, False, True],
        ]
        print(game.world)
        assert game.world == expected_next_world, "The world did not update correctly"

    def test_get_near(self) -> None:
        """
        Test that __get_near method counts the neighbors correctly.
        """
        game = GameOfLife(3, 3)
        test_world = [
            [True, False, False],
            [False, True, True],
            [False, False, True],
        ]

        # Test neighbor counting for the cell at (1, 1)
        neighbors = game._GameOfLife__get_near(  # type: ignore[attr-defined]
            test_world,
            (1, 1),
        )
        assert neighbors == 3, "Should have 3 neighbors for cell (1, 1)"

        # Test neighbor counting for the cell at (0, 0)
        neighbors = game._GameOfLife__get_near(  # type: ignore[attr-defined]
            test_world,
            (0, 0),
        )
        assert neighbors == 3, "Should have 3 neighbors for cell (0, 0)"

    def test_singleton_behavior(self) -> None:
        """
        Test that multiple instances of GameOfLife return the same object.
        """
        game1 = GameOfLife()
        game2 = GameOfLife()
        assert game1 is game2, "GameOfLife should be a singleton"

    def test_previous_world(self) -> None:
        """
        Test that previous world is updated correctly after forming a new generation.
        """
        game = GameOfLife(2, 2)

        initial_world = [
            [True, False],
            [False, True],
        ]
        game._GameOfLife__world = initial_world  # type: ignore[attr-defined]
        game.form_new_generation()  # Advance to the next generation

        # The previous world should hold the initial state
        assert (
            game.previous_world == initial_world
        ), "Previous world should match the initial state"
