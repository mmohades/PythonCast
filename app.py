#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

from flask import Flask, request
from flask_assistant import Assistant

from app.main.config import PROJECT_ID, PROJECT_TOKEN
from app.main.controller.voice_handlers import cast_intent
from app.main.controller.broadcast import youtube_broadcast

app = Flask(__name__)
assist = Assistant(app, route='/', client_token=PROJECT_TOKEN, project_id=PROJECT_ID)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']


@assist.action('CastIntent')
def casting(q):
    """

    :param q: The query extracted by Dialogflow
    :type q: str

    :returns: flask_assistant.tell
    """
    return cast_intent(q)


@app.route('/broadcast', methods=["POST"])
def take_action():
    """
    q should be provided as a param.
    :return: JSON
    """
    return youtube_broadcast(request)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)


