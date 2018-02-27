from src.bortiz import db
from flask_sqlalchemy import BaseQuery
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import SearchQueryMixin

class MessageQuery(BaseQuery, SearchQueryMixin):
    pass

class Message(db.Model):
    query_class = MessageQuery
    __tablename__ = 'messages'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger)
    message_date = db.Column(db.DateTime)
    message = db.Column(db.Text)
    search_vector = db.Column(TSVectorType('message'))


db.configure_mappers()
db.create_all()
db.commit()
