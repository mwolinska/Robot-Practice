from random import randint


class Robot:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.robot_id = randint(0, 1000)

    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age}. My ID is {self.robot_id}")

if __name__ == '__main__':
    my_robot = Robot("Troy", 2)
    my_robot.say_hello()
