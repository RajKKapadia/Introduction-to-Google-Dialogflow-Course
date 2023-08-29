from flask import Blueprint

home = Blueprint(
    'home',
    __name__
)

@home.route('/', methods=['GET', 'POST'])
def handle_home():
    return 'App working okay.', 200
