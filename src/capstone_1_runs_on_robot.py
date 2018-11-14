"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Alexander Harris.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DONE: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import math


def main():
    # --------------------------------------------------------------------------
    # DONE: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlETC(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()

class RemoteControlETC(object):
    """
    Stores the robot
        :type robot: rb.Snatch3rRobot
    """
    def __init__(self, robot):
        self.robot = robot
        self.direction = 0
        self.multiplier = 1
        self.speed = 100

    def speed_setup(self, speed_string):
        try:
            speed = int(speed_string)
        except:
            speed = 100

        self.speed = speed

    def multiplier_setup(self, multiplier_string):
        try:
            multiplier = int(multiplier_string)
        except:
            multiplier = 1

        self.multiplier = multiplier



    def coordinate_setup(self, coordinate_list):
        print("*****")
        print(coordinate_list)
        print("*****")

        list = []
        for k in range(0, len(coordinate_list)-1, 2):
            pointlist = []
            pointlist = pointlist + [coordinate_list[k]]
            pointlist = pointlist + [coordinate_list[k+1]]
            list = list + [pointlist]

        print("***Finished List***")
        print(list)
        print("***Finished List***")

        self.drive_start(list)

    def drive_start(self, list):
        if len(list) < 2:
            print(list)
            print("error")
            return

        for k in range(len(list)-1):
            xpos = list[k][0]
            ypos = list[k][1]
            xfpos = list[k+1][0]
            yfpos = list[k+1][1]
            x = xfpos - xpos
            y = yfpos - ypos
            if (x == 0) or (y == 0):
                if (x == 0):
                    self.robot.drive_system.go_straight_inches(((y/111)*self.multiplier), self.speed)
                else:
                    if (x < 0):
                        self.robot.drive_system.spin_in_place_degrees(-90)
                        self.robot.drive_system.go_straight_inches(((x/111)*self.multiplier), self.speed)
                        self.robot.drive_system.spin_in_place_degrees(90)
                    else:
                        self.robot.drive_system.spin_in_place_degrees(90)
                        self.robot.drive_system.go_straight_inches(((x/111)*self.multiplier), self.speed)
                        self.robot.drive_system.spin_in_place_degrees(-90)
            else:
                print("X move and Y move")
                print("X:", x)
                print("Y:", y)
                print("*****************")
                distance = math.sqrt(((x**2)+(y**2)))
                distance = ((distance/111) * self.multiplier)
                print("***Distance Traveling (in inches)***")
                print(distance)
                print("************************************")
                if (yfpos < ypos):
                    theta = math.atan(((abs(y)) / (abs(x))))
                    theta = ((theta * 180) / math.pi)
                    theta = 90 - theta
                else:
                    theta = math.atan(((abs(x)) / (abs(y))))
                    theta = ((theta * 180) / math.pi)
                    theta = 180 - theta
                print("***Turning Angle (in degrees)***")
                print(theta)
                print("********************************")
                if (x < 0):
                    self.robot.drive_system.spin_in_place_degrees(-theta)
                    self.robot.drive_system.go_straight_inches(distance,self.speed)
                    self.robot.drive_system.spin_in_place_degrees(theta)
                else:
                    self.robot.drive_system.spin_in_place_degrees(theta)
                    self.robot.drive_system.go_straight_inches(distance,self.speed)
                    self.robot.drive_system.spin_in_place_degrees(-theta)

    def go_forward(self, speed_string):
        try:
            speed = int(speed_string)
        except:
            speed = 100
        self.robot.drive_system.start_moving(speed,speed)


    def go_backward(self, speed_string):
        try:
            speed = int(speed_string)
            speed = -speed
        except:
            speed = -100

        self.robot.drive_system.start_moving(speed,speed)


    def spin_left(self, degree_string):
        try:
            degrees = int(degree_string)
            degrees = -degrees
        except:
            degrees = -90

        self.robot.drive_system.spin_in_place_degrees(degrees)


    def spin_right(self, degree_string):
        try:
            degrees = int(degree_string)
            degrees = degrees
        except:
            degrees = 90

        self.robot.drive_system.spin_in_place_degrees(degrees)


    def stop(self):
        self.robot.drive_system.stop_moving()


    def move_inches(self, inches_string):
        try:
            inches = int(inches_string)
        except:
            inches = 10

        self.robot.drive_system.go_straight_inches(inches)


    # def move_arm(self, position_string):
    #     try:
    #         position = int(position_string)
    #     except:
    #         position = 14.2
    #
    #     if position > 14.2:
    #         position = 14.2
    #     elif position < 0:
    #         position = 0
    #
    #     self.robot.arm.move_arm_to_position(position, 100)


main()