"""
  Capstone Project.  Code written by Ricardo Hernandez.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time

robot = rb.Snatch3rRobot()

def move_robot():
    robot.drive_system.go_straight_inches(10, 100)


def color():
    while True:
        x = robot.color_sensor.get_reflected_intensity()
        print(x)

def main():
    """ Runs YOUR specific part of the project """
    move_robot()
    color()

main()

