from flask import Blueprint
from flask import request, jsonify

from qna_chatbot.utils.helper_functions import format_response
from qna_chatbot.utils.action_handler import user_provides_difficulty_level, user_provides_answer, default_welcome_intent, start_again

dialogflow = Blueprint(
    'dialogflow',
    __name__
)

@dialogflow.route('/webhook', methods=['POST'])
def handle_webhook():
    body = request.get_json()
    action = body['queryResult']['action']
    if action == 'userProvidesDifficultyLevel':
        response_data = user_provides_difficulty_level(body)
    elif action == 'userProvidesAnswer':
        response_data = user_provides_answer(body)
    elif action == 'defaultWelcomeIntent':
        response_data = default_welcome_intent(body)
    elif action == 'startAgain':
        response_data = start_again(body)
    else:
        response_data = format_response(
            [
                f'No handler for the action {action}.'
            ]
        )
    return jsonify(response_data)
