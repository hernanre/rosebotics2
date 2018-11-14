
"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Alexander Harris.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DONE: 2. With your instructor, discuss the "big picture" of laptop-robot
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

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root,mqtt_client)

    root.mainloop()
    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------


def setup_gui(root_window,mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=50)
    frame.grid()

    label1 = ttk.Label(frame, text="Speed Value")
    label1.grid()

    speed_entry_box = ttk.Entry(frame)
    speed_entry_box.grid()

    go_forward_button = ttk.Button(frame, text="Go forward")
    go_forward_button.grid()
    go_backward_button = ttk.Button(frame, text="Go backward")
    go_backward_button.grid()

    label2 = ttk.Label(frame, text="Spin Value")
    label2.grid()

    spin_entry_box = ttk.Entry(frame)
    spin_entry_box.grid()

    spin_left_button = ttk.Button(frame, text="Spin left")
    spin_left_button.grid()
    spin_right_button = ttk.Button(frame, text="Spin right")
    spin_right_button.grid()

    stop_button = ttk.Button(frame, text="Stop")
    stop_button.grid()

    label3 = ttk.Label(frame, text="Inches Box")
    label3.grid()

    inches_entry_box = ttk.Entry(frame)
    inches_entry_box.grid()

    move_inches_button = ttk.Button(frame, text="Move Inches")
    move_inches_button.grid()
    # use_arm_button = ttk.Button(frame, text="Move Arm")
    # use_arm_button.grid()

    go_forward_button['command'] = (lambda: handle_go_forward(speed_entry_box,mqtt_client))
    go_backward_button['command'] = (lambda: handle_go_backward(speed_entry_box, mqtt_client))
    spin_left_button['command'] = (lambda: handle_spin_left(spin_entry_box, mqtt_client))
    spin_right_button['command'] = (lambda: handle_spin_right(spin_entry_box, mqtt_client))
    stop_button['command'] = (lambda: stop(mqtt_client))
    move_inches_button['command'] = (lambda: handle_move_inches(inches_entry_box, mqtt_client))
    # use_arm_button['command'] = (lambda: handle_move_arm(speed_entry_box, mqtt_client))

    root_window.bind_all('<Key-w>', lambda event: handle_go_forward(speed_entry_box, mqtt_client))
    root_window.bind_all('<Key-a>', lambda event: handle_spin_left(spin_entry_box, mqtt_client))
    root_window.bind_all('<Key-d>', lambda event: handle_spin_right(spin_entry_box, mqtt_client))
    root_window.bind_all('<Key-s'), lambda event: handle_go_backward(speed_entry_box, mqtt_client)
    root_window.bind_all('<Key-space>', lambda event: stop(mqtt_client))

    # root_window.bind('<Up>', lambda: handle_go_forward(speed_entry_box, mqtt_client))
    # root_window.bind('<Down>', lambda: handle_go_backward(speed_entry_box, mqtt_client))
    # root_window.bind('<Left>', lambda: handle_spin_left(speed_entry_box, mqtt_client))
    # root_window.bind('<Right>', lambda: handle_spin_right(speed_entry_box, mqtt_client))
    # root_window.bind('<space>', lambda: stop(mqtt_client))
    # root_window.bind('<i>', lambda: handle_move_inches(speed_entry_box, mqtt_client))


def handle_go_forward(entrybox,mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    # --------------------------------------------------------------------------
    # TODO: 6. This function needs the entry box in which the user enters
    # TODO:    the speed at which the robot should move.  Make the 2 changes
    # TODO:    necessary for the entry_box constructed in  setup_gui
    # TODO:    to make its way to this function.  When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 7. For this function to tell the robot what to do, it needs
    # TODO:    the MQTT client constructed in main.  Make the 4 changes
    # TODO:    necessary for that object to make its way to this function.
    # TODO:    When done, delete this TODO.
    # --------------------------------------------------------------------------

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

    speed = entrybox.get()
    # try:
    #     speed = int(speed)
    # except:
    #     print("This is not a integer")
    #     return
    mqtt_client.send_message('go_forward', [speed])
    print("sending 'go_forward' to the robot, with a speed", speed)

def handle_go_backward(entrybox, mttq_client):
    speed = entrybox.get()
    mttq_client.send_message('go_backward', [speed])
    print("sending 'go_backward' to the robot, with a speed", speed)

def handle_spin_left(entrybox, mttq_client):
    degrees = entrybox.get()
    mttq_client.send_message('spin_left', [degrees])
    print("sending 'spin_left' to the robot, with degrees", degrees)

def handle_spin_right(entrybox, mttq_client):
    degrees = entrybox.get()
    mttq_client.send_message('spin_right', [degrees])
    print("sending 'spin_right' to the robot, with degrees", degrees)

def stop(mttq_client):
    mttq_client.send_message('stop')
    print("sending 'stop' to the robot, with degrees")

def handle_move_inches(entrybox, mttq_client):
    inches = entrybox.get()
    mttq_client.send_message('move_inches', [inches])
    print("sending 'move_inches' to the robot, with inches", inches)

# def handle_move_arm(entrybox, mttq_client):
#     position = entrybox.get()
#     mttq_client.send_message('move_arm', [position])
#     print("sending 'move_arm' to the robot, with position", position)





main()
