import db as db
import sqlalchemy as sa

from sqlalchemy import Column, BigInteger, Text, DateTime
from sqlalchemy_utils.types import TSVectorType


class Message(db.Base):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    message_date = Column(DateTime)
    message = Column(Text)
    search_vector = Column(TSVectorType('message'))


sa.orm.configure_mappers()
db.Base.metadata.create_all(db.instance)
