import copy

import pytest  # noqa: F401

from game import GameOfLife


class TestGameOfLife:
    def test_generate_world(self) -> None:
        game = GameOfLife(5, 5)

        assert game.world
        assert game.previous_world
        assert game.life_count == 0

    def test_form_new_generation(self) -> None:
        game = GameOfLife(5, 5)
        prev_world = copy.deepcopy(game.world)
        game.form_new_generation()

        assert game.world != prev_world
        assert game.previous_world == prev_world
        assert game.life_count == 1

    def test_to_string(self) -> None:
        game = GameOfLife(5, 5)

        assert str(game) == f"GameOfLife<{id(game)}>[width:5, height:5, life_count:0]"
