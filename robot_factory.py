from random import randint

from data_model import RobotDesign
from robot import Robot
from world import World


class RobotFactory:
    def __init__(
        self,
        world: World,
        number_of_robots: int = 1,
        robot_design: RobotDesign = RobotDesign.RANDOM,
    ):
        self.world = world
        self.population = self._create_population(number_of_robots, robot_design)

    def _create_population(
        self,
        number_of_robots: int,
        robot_design: RobotDesign,
    ):
        list_of_robots = []
        for i in range(number_of_robots):
            new_robot = self.add_robot(robot_design)
            new_robot.robot_id = i
            list_of_robots.append(new_robot)
        return list_of_robots

    def add_robot(
        self,
        robot_design: RobotDesign,
    ):
        if robot_design == RobotDesign.RANDOM:
            return Robot.create_random(self.world)
        elif robot_design == RobotDesign.USER_INPUT:
            return Robot.create_from_user_input(self.world)
        else:
            raise NotImplementedError

    def deploy_all_robots_to_treasure_hunt(self):
        for robot in self.population:
            world = robot.find_treasure(self.world)
            self.world = world

        print("All robots found the treasure.")
