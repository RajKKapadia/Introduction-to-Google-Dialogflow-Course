from random import choice, choices
import json


from config import config


with open(config.QNA_FILE_PATH, 'rb') as file:
    qna = json.loads(file.read())


def get_parameters(body: dict, context_name: str) -> dict:
    output_contexts = body['queryResult']['outputContexts']
    parameters = {}
    for oc in output_contexts:
        name = oc['name']
        if context_name in name:
            parameters = oc['parameters']
    return parameters


def format_response(messages: list[str], output_contexts: list[dict] = []) -> dict:
    response_data = {
        'fulfillmentMessages': [
            {
                'text': {
                    'text': messages
                }
            }
        ]
    }
    if len(output_contexts) > 0:
        response_data['outputContexts'] = output_contexts
    return response_data


def get_error_message() -> dict:
    error_message = choice(config.ERROR_MESSAGES)
    response_data = format_response([error_message])
    return response_data


def get_random_qna(difficulty_level: str) -> list:
    try:
        random_qna = choices(
            list(qna[str(difficulty_level)].values()), k=config.NUMB_QUE_TO_ASK)
        return random_qna
    except:
        return []
