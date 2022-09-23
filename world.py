from typing import Tuple

import numpy as np

from data_model import Quadrants


class World:
    def __init__(self, size: tuple = (10, 10)):
        """Initliase World object.

        Args:
            size: tuple defining grid size of the world board in the order (row, column).
        """
        self.board = np.zeros((size[1], size[0]))

    def find_quadrant(self, position_tuple: Tuple[int, int]) -> Quadrants:
        """Return quadrant based on position in board.

        Args:
            position_tuple: position within the board in format (row, column).

        Returns:
            Quadrant within which the position is found.
        """
        if position_tuple[0] > self.board.shape[1] or position_tuple[1] > self.board.shape[0]:
            raise NameError("Desired position is outside of the board size")

        row_boundary = (self.board.shape[1] // 2)
        column_boundary = (self.board.shape[0] // 2)

        if position_tuple[0] < row_boundary and position_tuple[1] < column_boundary:
            return Quadrants.TOP_LEFT
        elif position_tuple[0] < row_boundary and position_tuple[1] > column_boundary:
            return Quadrants.TOP_RIGHT
        elif position_tuple[0] > row_boundary and position_tuple[1] < column_boundary:
            return Quadrants.BOTTOM_LEFT
        elif position_tuple[0] > row_boundary and position_tuple[1] > column_boundary:
            return Quadrants.BOTTOM_RIGHT

if __name__ == '__main__':
    new_world = World((1, 10))
    quadrant = new_world.find_quadrant((0, 1))
    print(quadrant)
