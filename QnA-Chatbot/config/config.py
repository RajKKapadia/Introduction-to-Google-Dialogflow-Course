import os

ERROR_MESSAGES = [
    'We are out of service at this point.',
    'We are facing an issue at this time.',
    'We are unable to serve you at this time.'
]

DIFFICULTY_LEVELS = [1, 2, 3, 4, 5]
NUMB_QUE_TO_ASK = 5

cwd = os.getcwd()

QNA_FILE_PATH = os.path.join(
    cwd,
    'data',
    'qna.json'
)
