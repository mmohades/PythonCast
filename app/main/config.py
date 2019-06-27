#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

import json

try:
    config_file = json.loads(open('config.json').read())
except FileNotFoundError:
    print("config.json file is missing!")


class Config:
    YOUTUBE_API_KEY = config_file["YoutubeKey"]
    ACTION_CLIENT_TOKEN = config_file["ActionToken"]
    ACTION_PROJECT_ID = config_file["ActionProjectId"]
    DEBUG = True


API_KEY = Config.YOUTUBE_API_KEY
PROJECT_TOKEN = Config.ACTION_CLIENT_TOKEN
PROJECT_ID = Config.ACTION_PROJECT_ID
