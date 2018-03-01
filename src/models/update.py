from src.bortiz import db
from sqlalchemy.dialects.postgresql.json import JSONB

class Update(db.Model):
    __tablename__ = 'updates'

    id = db.Column(db.BigInteger, primary_key=True)
    document = db.Column(JSONB)

db.configure_mappers()
db.create_all()
db.session.commit()

# sa.event.listen(Update.__tablename__, 'after_insert',
#                 DDL("""
#                     TRIGGER
#                 """)
#                 )
