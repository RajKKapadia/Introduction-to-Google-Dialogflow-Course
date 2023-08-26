from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'All is well.', 200


def get_parameters(body: dict) -> dict:
    output_contexts = body['queryResult']['outputContexts']

    for oc in output_contexts:
        name = oc['name']
        if 'session-vars' in name:
            print(oc['parameters'])
            return oc['parameters']
    return {}

@app.route('/webhook', methods=['POST'])
def webhook():
    print('We are hit')
    body = request.get_json()
    print(body)
    parameters = get_parameters(body)
    print(parameters)
    '''
    TODO
    (1) Exract the exact parameters
    (2) Save the parameters/ check the parameters, etc.
    (3) Generate the response and send it
    '''
    return jsonify(
        {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Thank you for the information."
                        ]
                    }
                }
            ]
        }
    )


if __name__ == '__main__':
    app.run(
        debug=True
    )
