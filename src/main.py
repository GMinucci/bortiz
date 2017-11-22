import requests
import time
import random

from flask import Flask

app = Flask(__name__)

next_offset = None

KEYWORDS = [
    '@ortiz_bot',
    '@dnlortz'
]


def get_answer():
    answers = [
        'hahahaha',
        'hahahahah',
        'aahahahaha',
        'hahahahahahah',
        'hahahahhahahah',
        'hahahahahahahahahaha',
        'hahahahahahhahahahaha',
        'ahahahahahahhahahahaha',
    ]

    return random.choice(answers)


def mentioned_me(msgs):
    which_are_channels = []

    mentions = list(filter(
                    lambda x: any(
                        w in x.get('message').get('text') for w in KEYWORDS
                        if 'message' in x
                        and 'text' in x.get('message')), msgs))

    for c in mentions:
        if not c['message']['chat']['id'] in which_are_channels:
            which_are_channels.append(c['message']['chat']['id'])

    if len(mentions) > 0:
        return which_are_channels
    else:
        return False


def is_funny(msgs):
    to_answer_channels = mentioned_me(msgs)

    if to_answer_channels:
        return to_answer_channels
    else:
        return False


def answser(channels, result=[]):
    if len(result) > 0 or len(result.result) > 0:
        for c_id in channels:
            payload = {
                'chat_id': c_id,
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

    json_response = r.get('result', None)

    if json_response and len(json_response) > 0:
        next_offset = json_response[-1]['update_id'] + 1

    return json_response


def start_bot():

    while True:
        result = get_updates()
        answer_to = is_funny(result)

        if len(result) > 0 and answer_to:
            time.sleep(5)
            answser(result=result, channels=answer_to)


start_bot()
