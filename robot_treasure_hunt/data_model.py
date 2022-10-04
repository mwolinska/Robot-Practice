from enum import Enum


class Quadrants (str, Enum):
    TOP_LEFT = "top left"
    TOP_RIGHT = "top right"
    BOTTOM_LEFT = "bottom left"
    BOTTOM_RIGHT = "bottom right"

class Compass(str, Enum):
    NORTH = "North"
    EAST = "East"
    SOUTH = "South"
    WEST = "West"
