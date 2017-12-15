import db as db
import sqlalchemy as sa
from sqlalchemy_searchable import make_searchable
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger
from sqlalchemy.dialects.postgresql import JSONB

make_searchable()
Base = declarative_base()


class Update(Base):
    __tablename__ = 'updates'

    id = Column(BigInteger, primary_key=True)
    update = Column(JSONB)


sa.orm.configure_mappers()
Base.metadata.create_all(db.instance)

# sa.event.listen(Update.__tablename__, 'after_insert',
#                 DDL("""
#                     TRIGGER
#                 """)
#                 )
