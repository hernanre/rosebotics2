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


def move_until_color(robot):
    while True:
        robot.drive_system.start_moving(50, 50)
        if robot.color_sensor.get_reflected_intensity() == robot.color_sensor.get_value(rb.Color.BLUE.value):
            robot.drive_system.stop_moving()
        break



def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    # move_robot(robot)
    color(robot)
    move_until_color(robot)


main()

