from flask import Flask
from flask_assistant import Assistant

from app.main.config import project_id, project_token


app = Flask(__name__)
assist = Assistant(app, route='/', client_token=project_token, project_id=project_id)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']


@assist.action('CastIntent')
def casting(q):
    pass


@app.route('/broadcast')
def take_action():
    pass


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
