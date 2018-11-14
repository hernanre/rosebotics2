
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

class PenData(object):
    def __init__(self):
        self.mouse_x = None
        self.mouse_y = None
        self.fclick = False
        self.list = []


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    pendata = PenData()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, pendata, mqtt_client)

    root.mainloop()

def setup_gui(root, pendata, mqtt_client):
    frame = ttk.Frame(root)
    frame.grid()
    label1 = ttk.Label(frame, text = "Draw points and click go!")
    label1.grid()
    canvas = tkinter.Canvas(frame, width = 500, height = 500, background='darkgrey')
    canvas.grid()
    button = ttk.Button(frame, text = "Go!")
    button.grid()
    label2 = ttk.Label(frame, text="Below is multiplier for inches traveling.")
    label2.grid()
    multiplier_box = ttk.Entry(frame, justify = tkinter.CENTER)
    multiplier_box.grid()
    label3 = ttk.Label(frame, text="Below is speed for driving.")
    label3.grid()
    speed_box = ttk.Entry(frame, justify = tkinter.CENTER)
    speed_box.grid()

    canvas.bind('<Button-1>', lambda event: mouseclick(event, canvas, pendata))
    button['command'] = (lambda: send_information(pendata, multiplier_box, speed_box, mqtt_client))

def mouseclick(event, canvas, pendata):
    canvas.create_oval(event.x - 3, event.y - 3,
                       event.x + 3, event.y + 3,
                       fill='black', width=0.5)
    if pendata.fclick == False:
        pendata.x = event.x
        pendata.y = event.y
        pendata.fclick = True
    else:
        canvas.create_line(pendata.x, pendata.y, event.x, event.y)
        pendata.x = event.x
        pendata.y = event.y

    pendata.list = pendata.list + [pendata.x]
    pendata.list = pendata.list + [pendata.y]

    print(pendata.list)

def send_information(pendata, multiplier_box, speed_box, mqtt_client):
    multiplier = multiplier_box.get()
    speed = speed_box.get()
    mqtt_client.send_message('multiplier_setup', [multiplier])
    mqtt_client.send_message('speed_setup', [speed])
    mqtt_client.send_message('coordinate_setup', [pendata.list])






main()