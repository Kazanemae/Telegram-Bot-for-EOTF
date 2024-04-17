from ORM.User import User as userModel
from ORM.Message import Message as messageModel
from ORM.db_connection import db, engine

def addNewUser(user_id):
    conn = engine.connect()
    select_msg = userModel.insert().values(user_id=user_id)
    conn.execute(select_msg)
    conn.commit()
    return conn.close()
def getUserById():
    conn = engine.connect()
    select_msg = db.select(messageModel).order_by(messageModel.columns.user_id)
    res = conn.execute(select_msg)
    conn.close()
    try:
        return res.fetchall()
    except Exception as e:
        return None
        print(e)

def addNessage(user_id, channel_id, channel_title, message_id):
    conn = engine.connect()
    select_msg = messageModel.insert().values(user_id=user_id,channel_id=channel_id,channel_title=channel_title,message_id=message_id)
    conn.execute(select_msg)
    conn.commit()
    return conn.close()

def getUserMessage(user_id, channel_id, message_id):
    conn = engine.connect()
    select_msg = db.select(messageModel).where(messageModel.columns.user_id==user_id,messageModel.columns.channel_id==channel_id,messageModel.columns.message_id==message_id,)
    res = conn.execute(select_msg)
    conn.close()
    try:
        return res.fetchall()[-1]
    except Exception as e:
        return None
        print(e)