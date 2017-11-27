import logging
import random
import time
import os

from telegram import MessageEntity
from telegram.ext import Updater, MessageHandler, Filters
from ortiz_mention_filter import ortiz_mention
from db import Message

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


def store_message(bot, update):



def echo(bot, update):
    time.sleep(8)
    bot.send_message(chat_id=update.message.chat_id, text=get_answer())


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

echo_handler = MessageHandler(Filters.text & ortiz_mention, echo)
dispatcher.add_handler(echo_handler)

storemessage_handler = MessageHandler(Filters.all, store_message)
dispatcher.add_handler(storemessage_handler)

updater.start_polling()
