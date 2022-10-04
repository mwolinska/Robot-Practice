import pytest

from robot_treasure_hunt.world import World
from robot_treasure_hunt.data_model import Quadrants


@pytest.mark.parametrize(["func_input", "expected_value"],
    [
        [(0, 0), Quadrants.TOP_LEFT],
        [(0, 7), Quadrants.TOP_RIGHT],
        [(6, 3), Quadrants.BOTTOM_LEFT],
        [(6, 7), Quadrants.BOTTOM_RIGHT],
    ]

)
def test_find_quadrant(func_input, expected_value):
    print(func_input)
    quadrant = World(size=(10, 10)).find_quadrant(func_input)
    assert quadrant == expected_value
