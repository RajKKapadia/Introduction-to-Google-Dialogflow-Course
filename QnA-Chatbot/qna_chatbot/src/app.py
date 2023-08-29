from flask import Flask

from qna_chatbot.views.home_route import home
from qna_chatbot.views.dialogflow_route import dialogflow

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(dialogflow)
