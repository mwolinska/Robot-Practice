from robot_treaure_hunt.robot_factory import RobotFactory
from robot_treaure_hunt.world import World


def run_from_file():
    new_world = World()
    robot_factory = RobotFactory.from_file(new_world, "../robot_names.txt")
    robot_factory.deploy_all_robots_to_treasure_hunt()

def run_from_user_input():
    new_world = World()
    robot_factory = RobotFactory.from_user_input(new_world, 1)
    robot_factory.deploy_all_robots_to_treasure_hunt()

def run_from_random():
    new_world = World()
    robot_factory = RobotFactory.from_random(new_world, 3)
    robot_factory.deploy_all_robots_to_treasure_hunt()

if __name__ == '__main__':
    run_from_user_input()
