"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.DriveSystem()
    robot.spin_in_place_degrees(90)
    robot.turn_degrees(70)


main()
