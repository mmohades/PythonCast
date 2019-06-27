#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

from .youtube_api import get_video_info
from ..util import browserController as Browser
from time import sleep
import threading


def broadcast_youtube(query):

    result = get_video_info(query)
    if result.confirmation == "Failed":
        return result

    t1 = threading.Thread(target=broadcast_link, args=(result.data["link"],))
    t1.start()

    return result


def broadcast_link(link):
    """
    open the link in browser.
    Full screen the browser. IF needed, close all the prev tabs.
    :param link:
    :return:
    """
    Browser.close_tab()
    Browser.open_in_browser(link)
    sleep(15)
    Browser.full_screen()

    return link
