"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    advanced_line_following()


def advanced_line_following():
    robot = rb.Snatch3rRobot()
    drivesystem = robot.drive_system
    colorsensor = robot.color_sensor

    drivesystem.start_moving(50,50)

    while True:
        if colorsensor.get_reflected_intensity() > 10:
            drivesystem.stop_moving()
            direction = test_water(robot,drivesystem,colorsensor)
            if direction == 0:
                print("There is no more line")
                drivesystem.stop_moving()
            else:
                drivesystem.spin_in_place_degrees(direction)
                drivesystem.start_moving(50,50)


def test_water(robot,drivesystem,colorsensor):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    list = [a,b,c,d,e,f]
    for k in range(len(list)):
        dir = -30 * (k+1)
        if dir < -90:
            dir = -dir

        drivesystem.spin_in_place_degrees(dir)
        drivesystem.go_straight_inches(10,50)
        if (colorsensor.get_reflected_intensity() < 20):
            list[k] = 1
        else:
            list[k] = 0
        drivesystem.go_straight_inches(10, -50)
        drivesystem.spin_in_place_degrees(-dir)

    # decision
    direction = 0
    for k in range(len(list)):
        if list[k] == 1:
            if k < 3:
                direction = direction - 30
            else:
                direction = direction + 30

        if direction == 0:
            return direction

        if direction > 30 or direction < -30:
            if direction == 90:
                direction = 60
            elif direction == 60:
                direction = 45
            elif direction == 30:
                direction = 30
            elif direction == -90:
                direction = -60
            elif direction == -60:
                direction = -45
            elif direction == -30:
                direction = -30

    return direction
main()
