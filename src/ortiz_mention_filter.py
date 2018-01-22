"""
    ortiz_mention_filter
"""
from telegram.ext import BaseFilter


class OrtizMention(BaseFilter):
    """ OrtizMention class """

    KEYWORDS = [
        '@ortiz_bot',
        '@dnlortz'
    ]

    def filter(self, message):
        """ filter function """
        return any(p in message.text for p in self.KEYWORDS)


ortiz_mention = OrtizMention()
