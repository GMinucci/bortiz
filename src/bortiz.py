import logging
import random
import time
import os

from telegram.ext import Updater, MessageHandler, Filters
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_searchable import make_searchable
from ortiz_mention_filter import ortiz_mention
from models.update import Update

app = Flask(__name__)

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE_URL = os.environ.get('DATABASE_URL')

if os.environ.get('ENV') == 'production':
    DATABASE_URL = os.environ.get('DATABASE_URL')
else:
    DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

make_searchable()

updater = Updater(os.environ.get('TOKEN'))
dispatcher = updater.dispatcher


def get_answer():
    initial = "ha" * (2 * random.randrange(2, 6))
    initial = list(initial)
    for i in range(0, 10):
        if bool(random.getrandbits(1)):
            initial[random.randrange(0, len(initial) - 1)] = \
                random.choice(["a", "h", "A", "H"])
    return "".join(initial)


def store_update(bot, update):
    data = Update(
        document=update.to_json()
    )

    db.session.add(data)
    db.session.commit()


def echo(bot, update):
    time.sleep(8)
    bot.send_message(chat_id=update.message.chat_id, text=get_answer())


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

echo_handler = MessageHandler(Filters.text & ortiz_mention, echo)
dispatcher.add_handler(echo_handler)

storemessage_handler = MessageHandler(Filters.all, store_update)
dispatcher.add_handler(storemessage_handler)

updater.start_polling()
