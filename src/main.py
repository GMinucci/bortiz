import requests
import time
import random

from flask import Flask

app = Flask(__name__)

next_offset = None

CHAT_ID = -180596549

KEYWORDS = [
    '@ortiz_bot',
    '@dnlortz'
]


def get_answer():
    answers = [
        'hahahaha',
        'hahahahah',
        'hahahahahahah',
        'hahahahhahahah',
        'hahahahahahahahahaha',
        'hahahahahahhahahahaha',
    ]

    return random.choice(answers)


def mentioned_me(msgs):
    mentions = list(filter(
                    lambda x: any(w in x['message']['text'] for w in KEYWORDS),
                    msgs))

    if len(mentions) > 0:
        return True
    else:
        return False


def is_funny(msgs):
    if mentioned_me(msgs):
        return True
    else:
        return False


def answser(result=[]):
    if len(result) > 0 or len(result.result) > 0:
        payload = {
            'chat_id': CHAT_ID,
            'text': get_answer()
        }

        requests.post('https://api.telegram.org/bot473779410:AAGLR'
                      'yTBCBj5fkrW1sYe_IF3mXcWVz1Rn3A/sendMessage',
                      data=payload)


def get_updates():
    json_response = []
    global next_offset
    offset = next_offset

    r = requests.post(f'https://api.telegram.org/bot473779410:AAGLR'
                      'yTBCBj5fkrW1sYe_IF3mXcWVz1Rn3A/getUpdates',
                      data={'offset': offset, 'timeout': 30}).json()

    json_response = r['result']

    if len(json_response) > 0:
        next_offset = json_response[-1]['update_id'] + 1

    return json_response


# @app.route('/')
def start_bot():

    while True:
        result = get_updates()

        if len(result) > 0 and is_funny(result):
            time.sleep(10)
            answser(result)


start_bot()
