from bortiz import db

class Update(db.Model):
    __tablename__ = 'updates'

    id = db.Column(db.BigInteger, primary_key=True)
    document = db.Column(db.JSONB)

db.configure_mappers()
db.create_all()
db.commit()

# sa.event.listen(Update.__tablename__, 'after_insert',
#                 DDL("""
#                     TRIGGER
#                 """)
#                 )
