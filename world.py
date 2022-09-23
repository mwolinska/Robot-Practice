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
