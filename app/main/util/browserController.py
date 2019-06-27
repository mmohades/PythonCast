#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

import webbrowser
import os
from time import sleep
from pynput.keyboard import Key, Controller
import platform

keyboard = Controller()


def press_key(key):
    """
    key must be a character or a Key
    :param key:
    :return:
    """

    if type(key) is not str and\
            type(key) is not Key or\
            (type(key) is str and len(key) != 1):
        raise TypeError

    keyboard.press(key)
    keyboard.release(key)


def open_in_browser(link):

    webbrowser.open(link, autoraise=True)


def close_tab():

    if platform.system() == "Darwin":
        keyboard.press(Key.cmd_l)
        keyboard.press('w')
        keyboard.release(Key.cmd_l)
        keyboard.release('w')
    else:
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release(Key.cmd_l)
        keyboard.release('w')


def close():

    browser_exe = "Google Chrome"
    os.system("pkill " + browser_exe)


def full_screen():

    press_key('f')


def forward():

    press_key(Key.right)


def backward():

    press_key(Key.left)


def pause():

    press_key(Key.space)


def mute():
    press_key('m')


def next_video():
    press_key('9')


def restart():
    press_key('0')


if __name__ == '__main__':

    # open_in_browser("https://www.youtube.com/watch?v=tAGnKpE4NCI")
    # sleep(5)
    # full_screen()
    # sleep(5)
    # close()
    sleep(5)
    close_tab()
