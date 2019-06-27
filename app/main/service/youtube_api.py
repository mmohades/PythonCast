#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

import requests
from ..config import API_KEY
from ..model.Response import Error, Success

API_LINK = "https://www.googleapis.com/youtube/v3/search?" \
       "part=snippet&" \
       "q={}&" \
       "key={}"
YOUTUBE_WATCH_LINK = "https://www.youtube.com/watch?v={}"


def get_video_info(query):

    video_data = {"name": "", "link": ""}

    resp = requests.get(API_LINK.format(query, API_KEY))
    items = resp.json()["items"]
    index = 0
    if len(items) < 1:
        return Error("No video found.")

    while items[index]["id"]["kind"] != "youtube#video":
        index += 1
        if index > len(items):
            return Error("No video found.")

    video_id = items[index]["id"]["videoId"]
    video_name = items[index]["snippet"]["title"]
    watch_link = YOUTUBE_WATCH_LINK.format(video_id)

    video_data["link"] = watch_link
    video_data["name"] = video_name

    print("Video found: " + video_name)

    return Success(video_data)
