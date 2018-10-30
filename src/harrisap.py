"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    # robot.drive_system.go_straight_inches(20)
    robot.drive_system.drive_polygon(8, 20)




# def drive_polygon(name, n, inches):
#     name = rb.Snatch3rRobot
#     degrees = ((n-2)*180)/n
#     for k in range(n):
#         name.drive_system.go_straight_inches(inches)
#         name.drive_system.turn_degrees(-degrees)




main()
