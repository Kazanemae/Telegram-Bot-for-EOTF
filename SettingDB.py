from Model.Setting import Message as settingModel
from Model.db_connection import db, engine

def addNewSetin(userbot_id, chat_id, from_date, chat_name):
    conn = engine.connect()
    select_msg = settingModel.insert().values(userbot_id=userbot_id, chat_id=chat_id, from_date=from_date, chat_name=chat_name, msg_count=0)
    conn.execute(select_msg)
    conn.commit()
    return conn.close()
def getAll():
    conn = engine.connect()
    select_msg = db.select(settingModel).order_by(settingModel.columns.msg_count)
    res = conn.execute(select_msg)
    conn.close()
    try:
        return res.fetchall()
    except Exception as e:
        return []


def deleteSetting(chat_id):
    conn = engine.connect()
    select_msg = db.delete(settingModel).where(settingModel.columns.chat_id==chat_id)
    res = conn.execute(select_msg)
    conn.commit()
    conn.close()
    try:
        return True
    except Exception as e:
        return False
        print(e)


def updateSetting(chat_id):
    conn = engine.connect()
    select_msg = db.update(settingModel).where(settingModel.columns.chat_id==chat_id).values(msg_count=1+settingModel.columns.msg_count)
    res = conn.execute(select_msg)
    conn.commit()
    conn.close()
    try:
        return True
    except Exception as e:
        return False
        print(e)

def updateSetting2(chat_id):
    conn = engine.connect()
    select_msg = db.update(settingModel).where(settingModel.columns.chat_id==chat_id).values(comment_count=1+settingModel.columns.comment_count)
    res = conn.execute(select_msg)
    conn.commit()
    conn.close()
    try:
        return True
    except Exception as e:
        return False
        print(e)

