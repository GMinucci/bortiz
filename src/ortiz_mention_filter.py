from telegram.ext import BaseFilter


class OrtizMention(BaseFilter):
    KEYWORDS = [
        '@ortiz_bot',
        '@dnlortz'
    ]

    def filter(self, message):
        return any(p in message.text for p in self.KEYWORDS)


ortiz_mention = OrtizMention()
