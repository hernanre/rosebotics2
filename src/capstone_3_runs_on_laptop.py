"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Thomas Nandola.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this
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

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 28
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
        self.color = 'blue'
        self.mouse_pos_x = None
        self.mouse_pos_y = None
        self.firstclick = False
        self.datalist = []


def main():
    pen_data = PenData()

    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    gui(root, mqtt_client,pen_data)


# --------------------------------------------------------------------------
# TODO: 5. Add code above that constructs a   com.MqttClient   that will
# TODO:    be used to send commands to the robot.  Connect it to this pc.
# TODO:    Test.  When OK, delete this TODO.
# --------------------------------------------------------------------------


# def setup_gui(root_window,mqtt_client):
#     """ Constructs and sets up widgets on the given window. """
#     frame = ttk.Frame(root_window, padding=10)
#     frame.grid()
#
#     speed_entry_box = ttk.Entry(frame)
#     go_forward_button = ttk.Button(frame, text="Go forward")
#
#     speed_entry_box.grid()
#     go_forward_button.grid()
#
#     go_forward_button['command'] = lambda: handle_go_forward(speed_entry_box, mqtt_client)

def gui(root, mqtt_client,pen_data):
    # Make root, frame and 3 buttons with callbacks.

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()


    intro = "Press <w> to go foward\n" \
            "\n" \
            + "Press <s> to go backwards\n" \
              "\n" \
            + "Press <d> to spin right\n" \
              "\n" \
            + "Press <a> to spin left.\n" \
              " \n" \
            + "Press <space> to stop\n"

    intro_label = ttk.Label(main_frame, text=intro)
    intro_label.grid()

    canvas = tkinter.Canvas(main_frame, background='lightgray', width=700, height=400)
    canvas.grid()

    canvas.bind('<Button-1>', lambda event: create_line(event,canvas,pen_data,mqtt_client))

    speed_entry_box = ttk.Entry(main_frame)
    set_speed_button = ttk.Button(main_frame, text="Set Speed")
    speed_entry_box.grid()
    set_speed_button.grid()

    degree_entry_box = ttk.Entry(main_frame)
    set_degree_button = ttk.Button(main_frame, text="Set Degree")
    degree_entry_box.grid()
    set_degree_button.grid()

    scale_entry_box = ttk.Entry(main_frame)
    set_scale_button = ttk.Button(main_frame, text="Set Scale")
    scale_entry_box.grid()
    set_scale_button.grid()

    clear_button = ttk.Button(main_frame, text="Clear")
    clear_button.grid()

    clear_button['command'] = lambda: clear_data(canvas,pen_data)

    drive_button = ttk.Button(main_frame, text="Drive!")
    drive_button.grid()

    drive_button['command'] = lambda: drive_info(speed_entry_box,scale_entry_box,pen_data,mqtt_client)

    root.bind_all('<Key-w>', lambda event: go_forward(speed_entry_box, mqtt_client))
    root.bind_all('<Key-s>', lambda event: go_backward(speed_entry_box, mqtt_client))
    root.bind_all('<Key-d>', lambda event: spin_right(degree_entry_box, mqtt_client))
    root.bind_all('<Key-a>', lambda event: spin_left(degree_entry_box, mqtt_client))
    root.bind_all('<Key-space>', lambda event: stop(mqtt_client))
    root.bind_all('(<KeyRelease>', lambda event: stop(mqtt_client))

    root.mainloop()


# keybind drive methods

def go_forward(speed_entry_box, mqtt_client):
    speed = speed_entry_box.get()
    print("Sending 'go forward' speed to the robot with speed", speed)
    mqtt_client.send_message('go_forward', [speed])


def go_backward(speed_entry_box, mqtt_client):
    speed = speed_entry_box.get()
    print("Sending 'go backward' speed to the robot with speed", speed)
    mqtt_client.send_message('go_backward', [speed])


def spin_right(degree_entry_box, mqtt_client):
    degree = degree_entry_box.get()
    print("Sending 'spin_right' degree to the robot with degree", degree)
    mqtt_client.send_message('spin_right', [degree])


def spin_left(degree_entry_box, mqtt_client):
    degree = degree_entry_box.get()
    print("Sending 'spin_left' degree to the robot with degree", degree)
    mqtt_client.send_message('spin_left', [degree])


def stop(mqtt_client):
    print("Sending 'stop' to the robot")
    mqtt_client.send_message('stop')

# canvas drawing methods


def create_line(event,canvas,data,mqtt_client):
    if data.firstclick == False:
        data.mouse_pos_x = event.x
        data.mouse_pos_y = event.y
        data.firstclick = True
        canvas.create_oval(event.x - 3, event.y - 3,
                           event.x + 3, event.y + 3,
                           outline='blue',fill='blue', width=3)
    else:
        canvas.create_line(data.mouse_pos_x, data.mouse_pos_y, event.x, event.y,fill=data.color,width=3)
        canvas.create_oval(event.x - 3, event.y - 3,
                           event.x + 3, event.y + 3,
                           outline='blue',fill='blue', width=3)
        data.mouse_pos_x = event.x
        data.mouse_pos_y = event.y

    data.datalist.append(data.mouse_pos_x)
    data.datalist.append(data.mouse_pos_y)

    if len(data.datalist) > 1:
        x_list = []
        y_list = []
        for k in range(0,len(data.datalist),2):
            x_list = x_list + [data.datalist[k]]
        for k in range(1,len(data.datalist),2):
            y_list = y_list + [data.datalist[k]]


        print("-------DATALIST---------")
        print(data.datalist)
        print("--------X_POINTS--------")
        print(x_list)
        print("--------Y_POINTS--------")
        print(y_list)
def clear_data(canvas,pen_data):
    canvas.delete("all")
    pen_data.datalist = []
    pen_data.mouse_pos_x = None
    pen_data.mouse_pos_y = None
    pen_data.firstclick = False


def drive_info(speed_entry_box,scale_entry_box,pen_data,mqtt_client):
    speed = speed_entry_box.get()
    scale = scale_entry_box.get()
    print(pen_data.datalist)
    mqtt_client.send_message('sequence_of_points',[speed,scale,pen_data.datalist])
    print("Message Sent!")


def received(message):
    print(message)

    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    # --------------------------------------------------------------------------
    # DONE: 6. This function needs the entry box in which the user enters
    # TODO:    the speed at which the robot should move.  Make the 2 changes
    # TODO:    necessary for the entry_box constructed in  setup_gui
    # TODO:    to make its way to this function.  When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # DONE: 7. For this function to tell the robot what to do, it needs
    # TODO:    the MQTT client constructed in main.  Make the 4 changes
    # TODO:    necessary for that object to make its way to this function.
    # TODO:    When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # DONE: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


main()
