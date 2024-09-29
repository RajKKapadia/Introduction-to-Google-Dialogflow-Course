from qna_chatbot.utils.helper_functions import format_response, get_parameters, get_random_qna, get_error_message
from config import config


def user_provides_difficulty_level(body: dict) -> dict:
    try:
        session = body['session']
        parameters = get_parameters(body, 'session-vars')
        difficulty_level = int(parameters['difficulty-level'])
        '''Check the difficulty level if not in difficulty levels response accordingly.
        '''
        if difficulty_level not in config.DIFFICULTY_LEVELS:
            output_contexts = [
                {
                    'name': f'{session}/contexts/await-difficulty',
                    'lifespanCount': 1
                }
            ]
            response_data = format_response(
                [
                    f'We do not have the level {difficulty_level} at this time.',
                    f'Please select a difficulty level between a number {min(config.DIFFICULTY_LEVELS)} to {max(config.DIFFICULTY_LEVELS)}.'
                ],
                output_contexts
            )
            return response_data
        else:
            '''Select 5 random question and ask the first question.
            Also set the parameters [counter, score, qna] in the output context for future use.
            '''
            random_qna = get_random_qna(str(difficulty_level))
            output_contexts = [
                {
                    'name': f'{session}/contexts/await-answer',
                    'lifespanCount': 1
                },
                {
                    'name': f'{session}/contexts/session-vars',
                    'lifespanCount': 20,
                    'parameters': {
                        'counter': 0,
                        'score': 0,
                        'random_qna': random_qna
                    }
                }
            ]
            response_data = format_response(
                [
                    'Here you go with your first question...',
                    f'(1) {random_qna[0]["question"][0]}'
                ],
                output_contexts
            )
            return response_data
    except:
        response_data = get_error_message()
        return response_data


def user_provides_answer(body: dict) -> dict:
    try:
        session = body['session']
        parameters = get_parameters(body, 'session-vars')
        user_answer = parameters['answer']
        counter = int(parameters['counter'])
        score = int(parameters['score'])
        random_qna = parameters['random_qna']
        '''Get the correct answer, calculate score, and increment the counter.
        For correct answer set the answer_flag
        '''
        answer_flag = False
        correct_answer = random_qna[counter]['prefferedAnswer'][0]
        if user_answer in random_qna[counter]['prefferedAnswer'] or user_answer in random_qna[counter]['alternateAnswers']:
            score += 1
            answer_flag = True
        counter += 1
        '''Check if the counter is greater than number of questions to ask.
        '''
        if counter > (config.NUMB_QUE_TO_ASK - 1):
            '''Correct answer, show the score and ask to start the quiz again.
            '''
            if answer_flag:
                output_contexts = [
                    {
                        'name': f'{session}/contexts/await-difficulty',
                        'lifespanCount': 1
                    }
                ]
                response_data = format_response(
                    [
                        f'Great, that is a right answer. High five!.',
                        f'Your score is {score} out of {config.NUMB_QUE_TO_ASK}.',
                        f'To start the quiz again please choose difficulty level of the question between a number {min(config.DIFFICULTY_LEVELS)} to {max(config.DIFFICULTY_LEVELS)}.'
                    ],
                    output_contexts
                )
                return response_data
            else:
                '''Wrong answer, show the score and ask to start the quiz again.
                '''
                output_contexts = [
                    {
                        'name': f'{session}/contexts/await-difficulty',
                        'lifespanCount': 1
                    }
                ]
                response_data = format_response(
                    [
                        f'Oops, that is a wrong answer.\nThe correct answer is {correct_answer}.',
                        f'Your score is {score} out of {config.NUMB_QUE_TO_ASK}.',
                        f'To start the quiz again please choose difficulty level of the question between a number {min(config.DIFFICULTY_LEVELS)} to {max(config.DIFFICULTY_LEVELS)}.'
                    ],
                    output_contexts
                )
                return response_data
        else:
            '''Counter is less than the number of questions we want to ask
            Ask the next question.
            '''
            output_contexts = [
                {
                    'name': f'{session}/contexts/await-answer',
                    'lifespanCount': 1
                },
                {
                    'name': f'{session}/contexts/session-vars',
                    'lifespanCount': 20,
                    'parameters': {
                        'counter': counter,
                        'score': score
                    }
                }
            ]
            if answer_flag:
                response_data = format_response(
                    [
                        f'Great, that is a right answer. Here is your next question.',
                        f'({counter + 1}) {random_qna[counter]["question"][0]}'
                    ],
                    output_contexts
                )
                return response_data
            else:
                response_data = format_response(
                    [
                        f'Oops, that is a wrong answer. The correct answe is {correct_answer}.',
                        'Here is your next question.',
                        f'({counter + 1}) {random_qna[counter]["question"][0]}'
                    ],
                    output_contexts
                )
                return response_data
    except:
        response_data = get_error_message()
        return response_data


def default_welcome_intent(body: dict) -> dict:
    session = body['session']
    output_contexts = [
        {
            'name': f'{session}/contexts/await-difficulty',
            'lifespanCount': 1
        },
        {
            'name': f'{session}/contexts/session-vars',
            'lifespanCount': 20
        }
    ]
    response_data = format_response(
        [
            'Welcome to High Five Maths!',
            f'We hope you will have fun learning with us. If you do not know he answer, just try your best and give it a go.',
            f'You will be asked {config.NUMB_QUE_TO_ASK} questions one by one.',
            'At what level do you want to start the quiz now?'
        ],
        output_contexts
    )
    return response_data


def start_again(body: dict) -> dict:
    session = body['session']
    output_contexts = [
        {
            'name': f'{session}/contexts/await-difficulty',
            'lifespanCount': 1
        },
        {
            'name': f'{session}/contexts/session-vars',
            'lifespanCount': 20
        }
    ]
    response_data = format_response(
        [
            'Great! You want to start again, here you go...',
            f'To start the quiz again type please choose difficulty level of the question between a number {min(config.DIFFICULTY_LEVELS)} to {max(config.DIFFICULTY_LEVELS)}.'

        ],
        output_contexts
    )
    return response_data
