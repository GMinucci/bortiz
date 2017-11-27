import os
import sqlalchemy as sa
from sqlalchemy import Integer, Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.environ.get('DATABASE_URL')

db = sa.create_engine(DATABASE_URL)
Base = declarative_base()
Session = sa.orm.sessionmaker(db)

make_searchable()


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    update = Column(JSONB)
    search_vector = Column(TSVectorType('message_text'))


sa.orm.configure_mappers()
Base.metadata.create_all(db)
