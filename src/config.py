import os


class Config(object):
    DEBUG = os.environ.get('DEBUG')
    TESTING = os.environ.get('TESTING')
    TOKEN = os.environ.get('TOKEN')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
