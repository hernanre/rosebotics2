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

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    rl = RemoteLaptop()
    mqtt_client = com.MqttClient(rl)
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)









    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=50)
    frame.grid()

    text = 'Press [W] to go FORWARD\n' \
           '\n' \
           'Press [S] to go BACKWARDS\n' \
           '\n' \
           'Press[D] to Turn RIGHT\n' \
           '\n' \
           'Press[A] to Turn LEFT\n' \
           '\n' \
           'Press [SPACE BAR] to STOP MOVING'

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

    notice1 = 'Press the button below to remove the focus away from the boxes above.'
    label = ttk.Label(frame, text=notice1)
    label.grid()

    key_mode_button = ttk.Button(frame, text='Key Arrow Mode')
    key_mode_button.grid()




    go_forward_button['command'] = lambda: handle_go_forward(speed_entry_box, mqtt_client)
    go_backwards_button['command'] = lambda: handle_backwards(speed_entry_box, mqtt_client)
    turn_left_button['command'] = lambda: handle_turn_left(left_box, mqtt_client)
    turn_right_button['command'] = lambda: handle_turn_right(right_box, mqtt_client)
    stop_button['command'] = lambda: handle_stop(mqtt_client)

    root_window.bind_all('<Key-w>', lambda event: handle_go_forward(speed_entry_box, mqtt_client))
    root_window.bind_all('<Key-s>', lambda event: handle_backwards(speed_entry_box, mqtt_client))
    root_window.bind_all('<Key-a>', lambda event: handle_turn_left(left_box, mqtt_client))
    root_window.bind_all('<Key-d>', lambda event: handle_turn_right(right_box, mqtt_client))
    root_window.bind_all('<Key-space>', lambda event: handle_stop(mqtt_client))
    root_window.bind_all('<Key-c>', lambda event: handle_get_color(mqtt_client))
    root_window.bind_all('<KeyRelease>', lambda event: handle_stop(mqtt_client))
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

def released_key(mqtt_client):
    print('You released the key you were pressing')
    mqtt_client.send_message('stop')

def handle_get_color(mqtt_client):
    print('Getting the color in front of me')
    mqtt_client.send_message('get_color')


class RemoteLaptop(object):
    def __init__(self):
        print('I got here')

    def robot_orange(self):
        print("I see orange")
        window = tkinter.Toplevel()
        photo = tkinter.PhotoImage(file='orange.gif')
        label = ttk.Label(window, image= photo)
        label.image = photo
        label.grid()

    def robot_yellow(self):
        print('I see yellow')
        window = tkinter.Toplevel()
        photo = tkinter.PhotoImage(file='Yellow.gif')
        label = ttk.Label(window, image=photo)
        label.image = photo
        label.grid()

    def robot_blue(self):
        print('I see blue')
        window = tkinter.Toplevel()
        photo = tkinter.PhotoImage(file='blue.gif')
        label = ttk.Label(window, image=photo)
        label.image = photo
        label.grid()

    def robot_red(self):
        print('I see red')
        window = tkinter.Toplevel()
        photo = tkinter.PhotoImage(file='red.gif')
        label = ttk.Label(window, image=photo)
        label.image = photo
        label.grid()

main()
