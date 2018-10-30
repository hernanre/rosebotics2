"""
  Capstone Project.  Code written by Ricardo Hernandez.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def move_robot(robot):
    robot.drive_system.go_straight_inches(10, 100)


def color(robot):
    while True:
        x = robot.color_sensor.get_reflected_intensity()
        print(x)
        break

def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    # move_robot(robot)
    color(robot)


main()

