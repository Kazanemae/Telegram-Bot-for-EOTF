from ORM.db_connection import  metadata, db

User = db.Table('user', metadata,
                    db.Column('user_id', db.Text()),
)