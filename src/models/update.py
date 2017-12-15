import db as db
import sqlalchemy as sa

from sqlalchemy import Column, BigInteger
from sqlalchemy.dialects.postgresql import JSONB


class Update(db.Base):
    __tablename__ = 'updates'

    id = Column(BigInteger, primary_key=True)
    document = Column(JSONB)


sa.orm.configure_mappers()
db.Base.metadata.create_all(db.instance)

# sa.event.listen(Update.__tablename__, 'after_insert',
#                 DDL("""
#                     TRIGGER
#                 """)
#                 )
