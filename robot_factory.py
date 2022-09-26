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
