"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
 

def main():
    """ Runs YOUR specific part of the project """


def CameraBeep():
    robot = rb.Snatch3rRobot()
    camera = robot.camera
    
    while True:
        width = camera.get_biggest_blob().width
        height = camera.get_biggest_blob().height

        area = width * height

        if area > 1000:
            ev3.Sound.beep()



    # print("untouched")
    # robot.touch_sensor.wait_until_pressed()
    # print("pressed")
    # robot.touch_sensor.wait_until_released()
    # print("released")
    #
    # print("sensor's measurement of reflected light intensity is greater than the given value")
    # robot.color_sensor.wait_until_intensity_is_less_than(6)
    # y = robot.color_sensor.get_reflected_intensity()
    # print(y)
    # print("sensor's measurement of reflected light intensity is less than the given value")
    #
    # print("sensor's measurement of reflected light intensity is less than the given value")
    # robot.color_sensor.wait_until_intensity_is_greater_than(6)
    # x = robot.color_sensor.get_reflected_intensity()
    # print(x)
    # print("sensor's measurement of reflected light intensity is greater than the given value")
    #
    # print("color?")
    # robot.color_sensor.wait_until_color_is(rb.Color.GREEN.value)
    # color = robot.color_sensor.get_color()
    # print(color)
    # print("found color!")
    #
    # print("color in a sequence?")
    # colors = [rb.Color.BLUE.value,rb.Color.RED.value,rb.Color.BROWN.value,rb.Color.YELLOW.value]
    # robot.color_sensor.wait_until_color_is_one_of(colors)
    # print("found color in sequence!")

def move_until_color(color):
    robot = rb.Snatch3rRobot()

    while True:
        robot.drive_system.start_moving()
        robot.color_sensor.wait_until_color_is(color)
        robot.drive_system.stop_moving()
        break
move_until_color(rb.Color.YELLOW.value)








    # # robot.color_sensor.get_colors()


main()
