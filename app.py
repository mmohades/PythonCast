from flask import Flask
from flask_assistant import Assistant

from app.main.config import PROJECT_ID, PROJECT_TOKEN
from app.main.controller.voice_handlers import cast_intent
from app.main.controller.broadcast import youtube_broadcast

app = Flask(__name__)
assist = Assistant(app, route='/', client_token=PROJECT_TOKEN, project_id=PROJECT_ID)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']


@assist.action('CastIntent')
def casting(q):
    return cast_intent(q)


@app.route('/broadcast', methods=['POST'])
def take_action():
    return youtube_broadcast()


if __name__ == '__main__':
    # app.run('0.0.0.0', debug=True)
    from app.main.service.casting_service import cast_youtube
    cast_youtube("Nothing else matters")

