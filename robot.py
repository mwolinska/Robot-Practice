from random import randint

class Robot:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.robot_id = randint(0, 1000)

    @classmethod
    def create_from_user_input(cls):
        robot_name = cls.get_name_from_input()
        robot_age = cls.get_age_from_input()
        return cls(robot_name, robot_age)

    @staticmethod
    def get_name_from_input():
        print("What is your robot's name?")
        new_name = input()
        return new_name

    @staticmethod
    def get_age_from_input():
        print("What is your robot's age?")
        new_age = int(input())
        return new_age

    @staticmethod
    def get_starting_position_from_input(world: World):
        print("Which row is your robot starting in?")
        row = int(input())
        print("Which column is your robot starting in?")
        column = int(input())
        return row, column

    @staticmethod
    def generate_random_starting_point(world: World):
        position_row = randint(0, world.board.shape[1] - 1)
        position_column = randint(0, world.board.shape[0] - 1)
        return position_row, position_column


    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age}. My ID is {self.robot_id}")
