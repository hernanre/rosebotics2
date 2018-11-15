"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and PUT_YOUR_NAME_HERE.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
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
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    robot = rb.Snatch3rRobot()

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
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
        time.sleep(0.01)  # For the delegate to do its work, let's messages get through.
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()


class RemoteControlEtc(object):

    def __init__(self,robot):
        """"
        Stores a robot
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
    # def go_forward(self,speed_string):
    #     speed = int(speed_string)
    #     print('Robot should start moving forwards.')
    #     self.robot.drive_system.start_moving(speed,speed)
    def go_forward(self,speed_string):
        speed = int(speed_string)
        print("Robot should start moving forward at speed,",speed)
        self.robot.drive_system.start_moving(speed,speed)
    def stop(self):
        print("Robot should come to a stop")
        self.robot.drive_system.stop_moving()
    def go_backward(self,speed_string):
        speed = int(speed_string)
        speed = -speed
        print('Robot should start moving backwards')
        self.robot.drive_system.start_moving(speed,speed)
    def spin_right(self,degree_string):
        degree = int(degree_string)
        print('Robot should start turning right')
        self.robot.drive_system.spin_in_place_degrees(degree)
    def spin_left(self,degree_string):
        degree = int(degree_string)
        degree = -degree
        print('Robot should start turning left')
        self.robot.drive_system.spin_in_place_degrees(degree)

#Robot Follow-Line Drive System

    def sequence_of_points(self,speed_string,scale_string,datalist):
        sq = []
        for k in range(0, len(datalist), 2):
            interior = []
            interior = interior + [datalist[k]]
            interior = interior + [datalist[k+1]]
            sq = sq + [interior]

        print(sq)

        self.drive_line(speed_string,scale_string,sq)

    def drive_line(self,speed_string,scale_string,sq):

        speed = int(speed_string)
        scale = int(scale_string)

        for k in range(len(sq) - 1):

            xi = sq[k][0]
            xf = sq[k + 1][0]

            yi = sq[k][1]
            yf = sq[k + 1][1]

            x_distance = (xf - xi)
            y_distance = (yf - yi)

            distance = math.sqrt(((x_distance) ** 2) + ((y_distance) ** 2))
            distance = (distance / 111) * scale
            print("Distance:")
            print(distance)

            if (yf < yi):
                angle = math.atan(((abs(y_distance)) / (abs(x_distance))))
                angle = ((angle * 180) / math.pi)
                angle = 90 - angle
            else:
                angle = math.atan(((abs(x_distance)) / (abs(y_distance))))
                angle = ((angle * 180) / math.pi)
                angle = 180 - angle
            md = distance/80
            md2 = 0
            if (x_distance < 0):
                self.robot.drive_system.spin_in_place_degrees(-angle)
                while True:
                    if md2 < distance:
                        self.robot.drive_system.go_straight_inches(md, speed)
                        md2 = md2 + md
                    else:
                        break

                    if ((70 * ((self.robot.proximity_sensor.get_distance_to_nearest_object())/100)) < 10):
                        self.robot.drive_system.stop_moving()
                        ev3.Sound.speak("Please Re Route!")
                        print("Re-Route")
                        return

                self.robot.drive_system.spin_in_place_degrees(angle)
            else:
                self.robot.drive_system.spin_in_place_degrees(angle)
                while True:
                    if md2 < distance:
                        self.robot.drive_system.go_straight_inches(md, speed)
                        md2 = md2 + md
                    else:
                        break

                    if ((70 * ((self.robot.proximity_sensor.get_distance_to_nearest_object()) / 100)) < 10):
                        self.robot.drive_system.stop_moving()
                        ev3.Sound.speak("Please Re Route!")
                        print("Re-Route")
                        return
                self.robot.drive_system.spin_in_place_degrees(-angle)



main()