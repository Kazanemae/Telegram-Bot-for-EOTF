from ORM.db_connection import  metadata, db

Message = db.Table('message', metadata,
                    db.Column('user_id', db.Text()),
                    db.Column('channel_id', db.Text()),
                    db.Column('channel_title', db.Text()),
                    db.Column('message_id', db.Text()),

)