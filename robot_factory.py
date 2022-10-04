import pathlib
from typing import Optional

from robot import Robot
from utils import find_number_of_lines_in_file, request_user_inputs
from world import World


class RobotFactory:
    def __init__(
        self,
        world: World,
    ):
        self.world = world
        self.list_of_robots = []
        self.__robot_generator = None

    @classmethod
    def from_file(cls, world, file_path_string: str):
        new_robot_factory = cls(world)
        number_of_robots = find_number_of_lines_in_file(pathlib.Path(file_path_string))
        generator, file = new_robot_factory.place_order(number_of_robots, pathlib.Path(file_path_string))
        new_robot_factory.build_order(generator, file)

        # robot_factory.robot_generator = robot_factory._robot_generator(pathlib.Path(file_path_string), robot_design=RobotDesign.FROM_FILE)
        # robot_generator = cls._robot_generator(pathlib.Path("file.txt"))
        # robot_factory._new_create_population(number_of_robots)

        return new_robot_factory

    @classmethod
    def from_random(cls, world: World, n_robots: int):
        # new_robot_factory = cls(world)
        # generator, file = new_robot_factory.place_order(n_robots, RobotDesign.RANDOM)
        # new_robot_factory.build_order(generator, file)
        pass

    @classmethod
    def from_user_input(cls, world: World, n_robots: int):
        pass

    def place_order(
            self,
            n_robots,
            file_path: Optional[pathlib.Path] = None,
            user_input: bool = False
    ): # return generator
        if file_path is not None:
            file = open(file=file_path)
            gen = self._robot_generator(n_robots, file)
            return gen, file
        else:
            gen = self._robot_generator(n_robots, user_input=user_input)
            return gen, None

    def build_order(self, generator, file = None):
        robot_idx = 1
        robot_constructor = next(generator)
        while robot_constructor is not None:
            new_robot = robot_constructor()
            new_robot.robot_id = robot_idx
            self.list_of_robots.append(new_robot)
            robot_constructor = next(generator)
            robot_idx += 1

        if file is not None:
            file.close()

    def _robot_generator(
            self,
            number_of_robots: int,
            file = None,
            user_input: bool = False,
    ): # TODO typing for generator

        for robot_index in range(number_of_robots):
            if file is not None:
                # file = file_name.open()
                robot_name = file.readline()
                robot_name = robot_name.rstrip()
                print(robot_name)
                robot_age = 1
                robot_position = (0, 0)
                # check world
                yield Robot.pre_build_robot(robot_name, robot_age, robot_position)
            elif user_input:
                name, age, position = request_user_inputs(self.world)
                yield Robot.pre_build_robot(name, age, position)
            else:
                yield lambda: Robot.create_random(self.world)
        print("should return none")
        yield None

    @property
    def robot_generator(self):
        return self.__robot_generator

    @robot_generator.setter
    def robot_generator(self, robot_generator):
        self.__robot_generator = robot_generator

    def deploy_all_robots_to_treasure_hunt(self):
        for robot in self.list_of_robots:
            world = robot.find_treasure(self.world)
            self.world = world

        print("All robots found the treasure.")

