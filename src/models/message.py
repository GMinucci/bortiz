import db as db
import sqlalchemy as sa
from sqlalchemy_searchable import make_searchable
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger, Text, DateTime
from sqlalchemy_utils.types import TSVectorType

make_searchable()
Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'

    id = Column(BigInteger)
    user_id = Column(BigInteger)
    message_date = Column(DateTime)
    message = Column(Text)
    search_vector = Column(TSVectorType('message'))


sa.orm.configure_mappers()
Base.metadata.create_all(db.instance)
