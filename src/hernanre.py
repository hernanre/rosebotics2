"""
  Capstone Project.  Code written by Ricardo Hernandez.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def move_robot(robot):
    robot.drive_system.go_straight_inches(10, 100)


def color(robot):
    while True:
        x = robot.color_sensor.get_reflected_intensity()
        print(x)
        break


def move_until_color(stop_color):
    robot = rb.Snatch3rRobot()
    drivesystem = robot.drive_system
    colorsensor = robot.color_sensor

    while True:
        drivesystem.start_moving(50, 50)
        colorsensor.wait_until_color_is(stop_color)
        drivesystem.stop_moving()
        break


def moving_arm_and_claw():
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw(100)


def calibrating():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate(100)


def move_to_pose():
    robot = rb.Snatch3rRobot()
    robot.arm.move_arm_to_position(3600, 100)

def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    move_robot(robot)
    # stop_color = rb.Color.BLUE.value
    # move_until_color(stop_color)
    moving_arm_and_claw()
    # calibrating()
    # move_to_pose()




