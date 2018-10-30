"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    print("untouched")
    robot.touch_sensor.wait_until_pressed()
    print("pressed")
    robot.touch_sensor.wait_until_released()
    print("released")
    # robot.color_sensor.get_color()
    # # robot.color_sensor.get_colors()


main()
