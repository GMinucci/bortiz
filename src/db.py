import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get('DATABASE_URL')

instance = sa.create_engine(DATABASE_URL)
Session = sessionmaker(instance)
