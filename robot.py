import copy
import random
from random import randint
from typing import Tuple

from data_model import Compass
from utils import get_name_from_input, get_age_from_input, get_starting_position_from_input, \
    generate_random_starting_point
from world import World

class Robot:
    def __init__(self, name: str, age: int, position: Tuple[int, int]):
        self.name = name
        self.age = age
        self.robot_id = randint(0, 100)
        self.position = position
        self.direction = random.choice(list(Compass))

    @classmethod
    def create_random(cls, world: World):
        robot_name = "Random Robot"
        robot_age = randint(0, 10)
        robot_position = generate_random_starting_point(world)
        return cls(robot_name, robot_age, robot_position)

    @classmethod
    def create_from_user_input(cls, world: World):
        robot_name = get_name_from_input()
        robot_age = get_age_from_input()
        robot_position = get_starting_position_from_input(world)
        return cls(robot_name, robot_age, robot_position)

    @staticmethod
    def get_name_from_input():
        print("What is your robot's name?")
        new_name = input()
        return new_name

    def observe(self, world: World):
        self.observations = world.get_observations(self.position)

    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age}. My ID is {self.robot_id}")

    def give_position_update(self, world: World):
        quadrant = world.find_quadrant(self.position)
        print(f"I am in position {self.position}, this is the {quadrant} quadrant. I am facing {self.direction}.")

    def find_treasure(self, world: World):
        self.say_hello()
        self.give_position_update(world)
        while self.position != world.treasure_position:
            world = self.go_forward(world)
            self.give_position_update(world)

        print("I found the treasure!")

    def go_forward(self, world: World) -> World:
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

        if new_row < 0 or new_row >= world.board.shape[1] or new_column < 0 or new_column >= world.board.shape[0]:
            print("Oh no, I hit a wall. I will turn 90 degrees.")
            self.turn_90_deg_clockwise()
        else:
            self.position = new_row, new_column
            world.board[new_row][new_column] = self.robot_id
            print(world.board)
        return world

    def turn_90_deg_clockwise(self):
        list_of_directions = list(Compass)
        direction_index = list_of_directions.index(self.direction)

        if direction_index == 3:
            direction_index = 0
        else:
            direction_index += 1

        self.direction = list_of_directions[direction_index]
