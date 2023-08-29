# QnA Chatbot
This is a repository for my course on `Google Dialogflow`.

### Setup
* create a new virtual environment using `Python3.10`
* activate it
* install all the packages from `requirements.txt` file

### How to run
* either run `python run.py` or `gunicorn run:app --bind 0.0.0.0:5000 --reload --log-level info`. You can access the application [here](http://localhost:5000/).

### Resources
You will find the following things from the repository.
* `qna_Agent.zip` is the Dialogflow agent
* Get the [NGROK](https://ngrok.com/)
* Create a [RENDER](https://render.com/) account to deploy the application.