import json

config_file = json.loads(open('config.json').read())


class Config:
    YOUTUBE_API_KEY = config_file["YoutubeKey"]
    ACTION_CLIENT_TOKEN = config_file["ActionToken"]
    ACTION_PROJECT_ID = config_file["ActionProjectId"]
    DEBUG = True


api_key = Config.YOUTUBE_API_KEY
project_token = Config.ACTION_CLIENT_TOKEN
project_id = Config.ACTION_PROJECT_ID
