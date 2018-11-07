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
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    """
    Stores the robot
    :type robot: rb.Snatch3rRobot
    """

    def __init__(self, robot):
        self.robot = robot

    def go_forward(self, speed_string):
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
main()