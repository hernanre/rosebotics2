"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Ricardo Hernandez.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this .
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=50)
    frame.grid()

    text = 'Press [W] to go FORWARD\n' \
           '\n' \
           'Press [S] to STOP\n' \
           '\n' \
           'Press[A] to Turn RIGHT\n' \
           '\n' \
           'Press[D] to Turn LEFT\n'
    label = ttk.Label(frame, text=text)
    label.grid()


    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go Forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_backwards_button = ttk.Button(frame, text="Go Backwards")
    notice = 'Goes backwards the same speed it goes forward'
    label = ttk.Label(frame, text=notice)
    label.grid()
    go_backwards_button.grid()


    left_box = ttk.Entry(frame)
    turn_left_button = ttk.Button(frame, text="Turn Left")
    left_box.grid()
    turn_left_button.grid()

    right_box = ttk.Entry(frame)
    turn_right_button = ttk.Button(frame, text="Turn Right")
    right_box.grid()
    turn_right_button.grid()

    stop_button = ttk.Button(frame, text="STOP")
    stop_button.grid()

    go_forward_button['command'] = lambda: handle_go_forward(speed_entry_box, mqtt_client)
    go_backwards_button['command'] = lambda: handle_backwards(speed_entry_box, mqtt_client)
    turn_left_button['command'] = lambda: handle_turn_left(left_box, mqtt_client)
    turn_right_button['command'] = lambda: handle_turn_right(right_box, mqtt_client)
    stop_button['command'] = lambda: handle_stop(mqtt_client)

    root_window.bind_all('<Key-w>', lambda event: handle_go_forward(speed_entry_box, mqtt_client))
    root_window.bind_all('<Key-a>', lambda event: handle_turn_left(left_box, mqtt_client))
    root_window.bind_all('<Key-d>', lambda event: handle_turn_right(right_box, mqtt_client))
    root_window.bind_all('<Key-space>', lambda event: handle_stop(mqtt_client))
    root_window.mainloop()


def handle_go_forward(speed_entry_box, mqtt_client):

    speed = speed_entry_box.get()
    print('sending go forward with the speed:', speed)

    mqtt_client.send_message('go_forward', [speed])
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
def handle_backwards(speed_entry_box, mqtt_client):
    go_backwards = speed_entry_box.get()
    print('Going backwards', go_backwards)
    mqtt_client.send_message('go_backwards', [go_backwards])



def handle_turn_left(left_box, mqtt_client):

    turn_left = left_box.get()
    print('turning left this many degrees:', turn_left)

    mqtt_client.send_message('turn_left_degrees', [turn_left])


def handle_turn_right(right_box, mqtt_client):
    turn_right = right_box.get()
    print('turning right this many degrees:', turn_right)

    mqtt_client.send_message('turn_right_degrees', [turn_right])


def handle_stop(mqtt_client):
    print('Stopping')
    mqtt_client.send_message('stop')



    # --------------------------------------------------------------------------
    # TODO: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


main()
