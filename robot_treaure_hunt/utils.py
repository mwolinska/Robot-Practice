import pathlib
from random import randint

from world import World


def get_name_from_input():
    print("What is your robot's name?")
    new_name = input()
    return new_name

def get_age_from_input():
    print("What is your robot's age?")
    new_age = int(input())
    return new_age

def get_starting_position_from_input(world: World):
    print("Which row is your robot starting in?")
    row = int(input())
    print("Which column is your robot starting in?")
    column = int(input())
    return row, column

def request_user_inputs(world: World):
    name = get_name_from_input()
    age = get_age_from_input()
    position = get_starting_position_from_input(world)
    return name, age, position

def generate_random_starting_point(world: World):
    position_row = randint(0, world.board.shape[1] - 1)
    position_column = randint(0, world.board.shape[0] - 1)
    return position_row, position_column

def find_number_of_lines_in_file(file_name: pathlib.Path) -> int:
    """Count number of lines in a file.

    Args:
        file_name: path to desired file.

    Returns:
        Number of lines in a file

    TODO:
        * (Marta): If there are empty lines between robot names they are counted as robots - handle potential bug.
    """
    file = file_name.open()
    line_counter = 0
    for line in file:
        line_counter += 1

    return line_counter
