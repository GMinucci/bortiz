import os

DATABASE_URL = os.environ.get('DATABASE_URL')
# POSTGRES_USER = os.environ.get('POSTGRES_USER')
# POSTGRES_DB = os.environ.get('POSTGRES_DB')
# POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

class Config(object):
    DEBUG = False
    TESTING = False
    TOKEN = os.environ.get('TOKEN')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
