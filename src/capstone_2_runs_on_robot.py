"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Ricardo Hernandez.
"""

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    george = com.MqttClient(rc)
    rc.mr = george
    george.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        time.sleep(0.01)  # For the delegate to do its work
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('You pressed the blue button')

class RemoteControlEtc(object):
    """
    Stores the robot
    :type robot: rb.Snatch3rRobot
    """

    def __init__(self, robot):
        self.robot = robot
        self.mr = None
    def go_forward(self, speed_string):
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def go_backwards(self, speed_string):
        speed = -int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def turn_left_degrees(self, turn_left_string):
        degrees = int(turn_left_string)
        self.robot.drive_system.spin_in_place_degrees(-degrees)

    def turn_right_degrees(self, turn_right_string):
        degrees = int(turn_right_string)
        self.robot.drive_system.spin_in_place_degrees(degrees)

    def stop(self):
        self.robot.drive_system.stop_moving()

    def get_color(self):
        self.robot.camera.set_signature('SIG1')
        red = self.robot.camera.get_biggest_blob()
        self.robot.camera.set_signature('SIG2')
        orange = self.robot.camera.get_biggest_blob()
        self.robot.camera.set_signature('SIG3')
        yellow = self.robot.camera.get_biggest_blob()
        self.robot.camera.set_signature('SIG5')
        blue = self.robot.camera.get_biggest_blob()


        if red.get_area() > 1000:
            self.mr.send_message("robot_red")
        if orange.get_area() > 1000:
            self.mr.send_message("robot_orange")
        if yellow.get_area() > 1000:
            self.mr.send_message("robot_yellow")
        if blue.get_area() > 1000:
            self.mr.send_message("robot_blue")

main()