from enum import Enum


class Quadrants (str, Enum):
    TOP_LEFT = "top left"
    TOP_RIGHT = "top right"
    BOTTOM_LEFT = "bottom left"
    BOTTOM_RIGHT = "bottom right"

class RobotDesign(str, Enum):
    USER_INPUT = "user input"
    RANDOM = "random"
    FROM_FILE = "from file"

class Compass(str, Enum):
    NORTH = "North"
    SOUTH = "South"
    WEST = "West"
    EAST = "East"
