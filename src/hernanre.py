"""
  Capstone Project.  Code written by Ricardo Hernandez.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


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


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(entry_box, mqtt_client)

    turn_left_button = ttk.Button(frame, text='Turn Left (degrees)')

    turn_left_button.grid()
    turn_left_button['command'] = lambda: handle_turn_left(entry_box, mqtt_client)

    turn_right_button = ttk.Button(frame, text='Turn Right(degrees)')
    turn_right_button.grid()
    turn_right_button['command'] = lambda: handle_turn_right(entry_box, mqtt_client)

    stop_button = ttk.Button(frame, text='Stop')
    stop_button.grid()
    stop_button['command'] = lambda: handle_stop(mqtt_client)


def handle_go_forward(speed_entry_box, mqtt_client):
    speed = speed_entry_box.get()
    print('sending go forward with the speed:', speed)

    mqtt_client.send_message('go_forward', [speed])
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """


def handle_turn_left(entry_box, mqtt_client):
    turn_left = entry_box.get()
    print('turning left this many degrees:', turn_left)

    mqtt_client.send_message('turn_left_degrees', [turn_left])


def handle_turn_right(entry_box, mqtt_client):
    turn_right = entry_box.get()
    print('turning right this many degrees:', turn_right)

    mqtt_client.send_message('turn_right_degrees', [turn_right])


def handle_stop(mqtt_client):
    print('Stopping')
    mqtt_client.send_message('stop')


def main():
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()

    robot = rb.Snatch3rRobot()
    move_robot(robot)
    # stop_color = rb.Color.BLUE.value
    # move_until_color(stop_color)
    moving_arm_and_claw()
    # calibrating()
    # move_to_pose()







