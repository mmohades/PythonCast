import webbrowser
import os
from time import sleep
from pynput.keyboard import Key, Controller


def press_key(key):
    """
    key must be a character or a Key
    :param key:
    :return:
    """
    keyboard = Controller()

    if type(key) is not str and\
            type(key) is not Key or\
            (type(key) is str and len(key) != 1):
        raise TypeError

    keyboard.press(key)
    keyboard.release(key)


def open_in_browser(link):

    # chromium_path = "/usr/bin/chromium-browser"
    # webbrowser.register('chromium', None, webbrowser.BackgroundBrowser(chromium_path), 1)
    browser = webbrowser#.get('chromium')

    browser.open(link, autoraise=True)


def close_tabs():

    browser_exe = "chromium-browse"
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

    open_in_browser("https://www.youtube.com/watch?v=tAGnKpE4NCI")
    sleep(5)
    full_screen()
    sleep(5)
    close_tabs()
