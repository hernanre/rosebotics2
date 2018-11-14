"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    red = rb.Color.RED.value
    blue = rb.Color.BLUE.value
    green = rb.Color.GREEN.value
    nocolor = rb.Color.NO_COLOR.value
    brown = rb.Color.BROWN.value
    white = rb.Color.WHITE.value
    yellow = rb.Color.YELLOW.value
    black = rb.Color.BLACK.value

    # robot = rb.Snatch3rRobot()
    # robot.drive_system.go_straight_inches(20)
    drive_polygon(5, 10)
    # line_follow()
    # drive_until_color(red)
    # robot.drive_system.turn_degrees
    #detectItem()
    # ColorSorting(red, blue, green, yellow, green)

def detectItem():
    robot = rb.Snatch3rRobot()
    sensor = robot.proximity_sensor

    while True:
        if ((70 * ((sensor.get_distance_to_nearest_object())/100)) < 15) and ((70 * ((sensor.get_distance_to_nearest_object())/100)) > 9):
            ev3.Sound.beep()



def drive_polygon(n, inches):
    x = rb.Snatch3rRobot()
    drivesystem = x.drive_system
    # degrees = ((n - 2) * 180) / n
    # degrees = 180 - degrees
    degrees = (360/n)

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
            drivesystem.spin_in_place_degrees(10)
            drivesystem.start_moving(50,50)


def drive_until_color(color):
    robot = rb.Snatch3rRobot()
    drivesystem = robot.drive_system
    colorsensor = robot.color_sensor
    drivesystem.start_moving(50,50)

    while True:
        colorsensor.wait_until_color_is(color)
        drivesystem.stop_moving()
        break




# Capstone Project

def ColorSorting(red, white, yellow, black, green):
    robot = rb.Snatch3rRobot()
    colorsensor = robot.color_sensor
    drivesystem = robot.drive_system
    ev3.Sound.set_volume(100)
    drivesystem.start_moving(20,20)

    while True:
        if colorsensor.get_color() == red:
            ev3.Sound.speak("Hello")
        if colorsensor.get_color() == white:
            ev3.Sound.speak("to")
        if colorsensor.get_color() == yellow:
            ev3.Sound.speak("the")
        if colorsensor.get_color() == black:
            ev3.Sound.speak("world")
        if colorsensor.get_color() == green:
            ev3.Sound.speak("Greetings humans")





























main()
