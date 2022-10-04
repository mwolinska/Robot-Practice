import copy
import random
from random import randint
from typing import Tuple

from robot_treaure_hunt.data_model import Compass
from robot_treaure_hunt.utils import get_name_from_input, get_age_from_input, \
    get_starting_position_from_input, \
    generate_random_starting_point
from robot_treaure_hunt.world import World


class Robot:
    def __init__(
        self, name: str,
        age: int,
        position: Tuple[int, int],
    ):
        """Intialise Robot class.

        This class will allow the robot to interact with the world
        to search for a treasure

        Args:
            name: robot's name.
            age: robot's age.
            position: robot's position.
        """
        self.name = name
        self.age = age
        self.robot_id = randint(0, 100)
        self.position = position
        self.direction = random.choice(list(Compass))
        # self.observations = {}

    @classmethod
    def create_random(cls, world: World):
        """Create a Robot instance with random inputs.

        Args:
            world: instance of World in which the Robot exists.
        """
        robot_name = "Random Robot"
        robot_age = randint(0, 10)
        robot_position = generate_random_starting_point(world)
        return cls(robot_name, robot_age, robot_position)

    @classmethod
    def create_from_user_input(cls, world: World):
        """Create a Robot instance from user input.

        Args:
            world: instance of World in which the Robot exists.

        Returns:
            An instance of Robot from user inputs.
        """
        robot_name = get_name_from_input()
        robot_age = get_age_from_input()
        robot_position = get_starting_position_from_input(world)
        return cls(robot_name, robot_age, robot_position)

    @classmethod
    def pre_build_robot(
        cls,
        robot_name: str,
        robot_age: int,
        robot_position: Tuple[int, int],
    ):
        """Prepare a function which will allow the robot to be built.

        In order to

        Args:
            robot_name: desired robot name.
            robot_age: desired robot age.
            robot_position: desired starting position of the robot.

        Returns:
            A function, which when run will return an instance of a Robot
             with the preset parameters.
        """
        def build_robot():
            return cls(robot_name, robot_age, robot_position)
        return build_robot

    # def observe(self, world: World):
    #     self.observations = world.get_observations(self.position)

    def say_hello(self):
        """Print welcome message with the robot's information."""
        print(f"Hello my name is {self.name}, my age is {self.age}. "
              f"My ID is {self.robot_id}")

    def give_position_update(self, world: World):
        """Print position, quadrant and the robot's direction."""
        # self.observe(world)
        quadrant = world.find_quadrant(self.position)
        print(f"I am in position {self.position}, this is the {quadrant} "
              f"quadrant. I am facing {self.direction}.")

    def find_treasure(self, world: World):
        """Launch the search for the treasure.

        The robot's objective is to find the treasure hidden in the world.
        It does so by going forward un

        """
        self.say_hello()
        self.give_position_update(world)
        while self.position != world.treasure_position:
            world = self.go_forward(world)
            self.give_position_update(world)
        print("I found the treasure!")
        return world

    def go_forward(self, world: World) -> World:
        """Move robot forwards until a wall is hit."""
        new_row = copy.deepcopy(self.position[0])
        new_column = copy.deepcopy(self.position[1])

        if self.direction == Compass.NORTH:
            new_row -= 1
        elif self.direction == Compass.SOUTH:
            new_row += 1
        elif self.direction == Compass.WEST:
            new_column -= 1
        elif self.direction == Compass.EAST:
            new_column += 1

        if new_row < 0 \
                or new_row >= world.board.shape[1] \
                or new_column < 0 \
                or new_column >= world.board.shape[0]:
            print("Oh no, I hit a wall. I will turn 90 degrees.")
            self.turn_90_deg_clockwise()
        else:
            self.position = new_row, new_column
            world.board[new_row][new_column] = self.robot_id
            print(world.board)
        return world

    def turn_90_deg_clockwise(self):
        """Change robot direction by 90 degrees clockwise following compass."""
        list_of_directions = list(Compass)
        direction_index = list_of_directions.index(self.direction)

        if direction_index == 3:
            direction_index = 0
        else:
            direction_index += 1

        self.direction = list_of_directions[direction_index]
