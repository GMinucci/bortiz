import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy_searchable import make_searchable
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = os.environ.get('DATABASE_URL')

instance = sa.create_engine(DATABASE_URL)
Session = sessionmaker(instance)
Base = declarative_base()

make_searchable()
