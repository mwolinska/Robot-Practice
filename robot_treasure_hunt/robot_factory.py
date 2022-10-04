import pathlib
from typing import Optional, Generator, TextIO

from robot_treasure_hunt.robot import Robot
from robot_treasure_hunt.utils import find_number_of_lines_in_file, \
    request_user_inputs
from robot_treasure_hunt.world import World


class RobotFactory:
    def __init__(
        self,
        world: World,
    ):
        self.world = world
        self.list_of_robots = []
        self.__robot_generator = None

    @classmethod
    def from_file(cls, world: World, file_path_string: str):
        """Create a robot factory with a robot list populated from a file.

        Args:
            world: world instance.
            file_path_string: path to file containing robot parameters.

        Returns:
            RobotFactory instance ready for the treasure hunt.
        """
        new_robot_factory = cls(world)
        file_path = pathlib.Path(file_path_string)
        number_of_robots = find_number_of_lines_in_file(file_path)
        generator, file = new_robot_factory.place_order(
            number_of_robots,
            file_path,
        )
        new_robot_factory.build_order(generator, file)

        # robot_factory.robot_generator = robot_factory._robot_generator(pathlib.Path(file_path_string), robot_design=RobotDesign.FROM_FILE)
        # robot_generator = cls._robot_generator(pathlib.Path("file.txt"))
        # robot_factory._new_create_population(number_of_robots)

        return new_robot_factory

    @classmethod
    def from_random(
        cls,
        world: World,
        n_robots: int,
    ):
        """Create a robot factory with a robot list populated from a file.

        Args:
            world: world instance.
            n_robots: desired number of robots in the factory.

        Returns:
            RobotFactory instance ready for the treasure hunt.
        """
        new_robot_factory = cls(world)
        generator, file = new_robot_factory.place_order(n_robots)
        new_robot_factory.build_order(generator, file)
        return new_robot_factory

    @classmethod
    def from_user_input(
        cls,
        world: World,
        n_robots: int,
    ):
        """Create a robot factory with from user input in the terminal.

        Args:
            world: world instance.
            n_robots: desired number of robots in the factory.

        Returns:
            RobotFactory instance ready for the treasure hunt.
        """
        new_robot_factory = cls(world)
        generator, file = new_robot_factory.place_order(
            n_robots,
            user_input=True,
        )
        new_robot_factory.build_order(generator, file)
        return new_robot_factory

    def place_order(
        self,
        number_of_robots: int,
        file_path: Optional[pathlib.Path] = None,
        user_input: bool = False,
    ):
        """Set parameters for the generator to build the desired robots.

        Args:
            number_of_robots: number of robots to be produced in order.
            file_path: pathlib object to the file containing robot parameters,
                if applicable.
            user_input: boolean to determine whether to create robots from
                user_input or randomly.
        """
        if file_path is not None:
            file = open(file=file_path)
            gen = self._robot_generator(number_of_robots, file)
            return gen, file
        else:
            gen = self._robot_generator(
                number_of_robots,
                user_input=user_input,
            )
            return gen, None

    def build_order(self, order: Generator, file: TextIO = None):
        """Build robots to the correct order.

        Args:
            order: robot generator with the desired order parameters.
            file: optional file like object containing robot parameters.

        Returns:
        """
        robot_idx = 1
        robot_constructor = next(order)
        while robot_constructor is not None:
            new_robot = robot_constructor()
            new_robot.robot_id = robot_idx
            self.list_of_robots.append(new_robot)
            robot_constructor = next(order)
            robot_idx += 1

        if file is not None:
            file.close()

    def _robot_generator(
            self,
            number_of_robots: int,
            file: Optional[TextIO] = None,
            user_input: bool = False,
    ):
        """Generator of Robot constructors.

        Args:
            number_of_robots: number of robots produced in the factory.
            file: file-like object containing robot parameters.
            user_input: boolean to determine whether to create robots from
                user_input or randomly.
        Returns:
            Constructor for Robot class.
        TODO:
            * (Sacha): can you help me write the docstring.
        """
        for robot_index in range(number_of_robots):
            if file is not None:
                robot_name = file.readline()
                robot_name = robot_name.rstrip()
                robot_age = 1
                robot_position = (0, 0)
                # check world
                yield Robot.pre_build_robot(
                    robot_name,
                    robot_age,
                    robot_position,
                )
            elif user_input:
                name, age, position = request_user_inputs(self.world)
                yield Robot.pre_build_robot(name, age, position)
            else:
                yield lambda: Robot.create_random(self.world)
        yield None

    def deploy_all_robots_to_treasure_hunt(self):
        """Start treasure hunt for all robots.

        Sequentially launches all robots from self.list_of_robots to
        complete the treasure hunt.

        """
        for robot in self.list_of_robots:
            world = robot.find_treasure(self.world)
            self.world = world

        print("All robots found the treasure.")

    @property
    def robot_generator(self):
        return self.__robot_generator

    @robot_generator.setter
    def robot_generator(self, robot_generator):
        self.__robot_generator = robot_generator
