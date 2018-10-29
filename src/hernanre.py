"""
  Capstone Project.  Code written by Ricardo Hernandez.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def move_robot():
    print('bye')
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(10, 100)

def main():
    """ Runs YOUR specific part of the project """
    print('hello')
    move_robot()

main()

