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
    # robot.drive_system.drive_polygon(8, 20)
    # line_follow()
    drive_until_color(rb.Color.NO_COLOR.value)

def drive_polygon(n, inches):
    x = rb.Snatch3rRobot()
    drivesystem = x.drive_system
    degrees = ((n - 2) * 180) / n
    degrees = 180 - degrees
    for k in range(n):
        drivesystem.go_straight_inches(inches)
        drivesystem.spin_in_place_degrees(-degrees)


def line_follow():
    robot = rb.Snatch3rRobot()
    drivesystem = robot.drive_system
    colorsensor = robot.color_sensor

    drivesystem.start_moving()
    while True:
        if colorsensor.get_reflected_intensity() > 10:
            drivesystem.spin_in_place_degrees(-10)
            drivesystem.start_moving(50,50)

def drive_until_color(color):
    robot = rb.Snatch3rRobot()
    drivesystem = robot.drive_system
    colorsensor = robot.color_sensor

    while True:
        drivesystem.start_moving(50,50)
        colorsensor.wait_until_color_is(color)
        drivesystem.stop_moving()
        break


main()
