port asyncio
import datetime
import os.path
import threading
import time

import nest_asyncio
import telebot
import schedule
from telebot.types import InputFile
from telethon.errors import UsernameInvalidError

nest_asyncio.apply()
bot = telebot.TeleBot("6774379680:AAFuml4xnoY3iTPW-s6K8N8PGVj6N_LpAGw", parse_mode=None)
from ORM.db_connection import metadata, engine
print("#bd connection")

print('#succes bd connection')
from telethon import TelegramClient
from telethon import errors, events
from ORM.dto import getUserById, getUserMessage, addNewUser, addNessage

links = [
    'https://t.me/hack_less',
    'https://t.me/xakerpro',
    'https://t.me/vx_virus_and_soft',
    'https://telegram.me/HNews',
    'https://t.me/CyberStrikeNews',
    'https://t.me/androidMalware',
    'https://t.me/itsecalert',
]


@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    print("#start рассылки")
    if(message.text == "поллучить колличество сообщений"):
        bot.reply_to(message, "введите колличетсво последних сообщений")
        return bot.register_next_step_handler(message, getMessage)
    addNewUser(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('поллучить колличество сообщений')
    bot.reply_to(message, "Вы теперь есть в рассылке", reply_markup=keyboard)

def getMessage(message):
    try:
        msgCount = int(message.text)
        asyncio.set_event_loop(loop1)
        asyncio.run(getMessages(1, msgCount,message.chat.id))
    except Exception as e:
        if isinstance(e, UsernameInvalidError):
            return
        print('error', e, type(e))
        bot.reply_to(message, "число не валидное проьбуйте еще")
        return bot.register_next_step_handler(message, getMessage)
#client.run_until_disconnected()
async def getMessages(type,filterCount, user_id = None):
    asyncio.set_event_loop(loop1)

    for i in links:
        entity = await client.get_entity(i)
        users = getUserById()
        if type == 1:
            async for msg in client.iter_messages(entity, reverse=True,
                                                  limit=filterCount):
                if not msg.message:
                    continue
                print('1', msg)
                print(msg.media)
                if msg.media:
                    try:
                        filename = msg.media.document.attributes[0].file_name
                        if not os.path.exists(filename):
                            doc = await client.download_media(msg)
                        else:
                            doc = InputFile(filename)
                            print(f"#файл пользователю {user_id} {entity.title} {entity.id}")
                            bot.send_document(int(user_id), document=doc)
                            bot.send_message(int(user_id), msg.message)
                    except:
                        doc = await client.download_media(msg)
                        print(f"#картинка пользователю {user_id} {entity.title} {entity.id}")
                        image = InputFile(str(doc))
                        bot.send_document(int(user_id), document=image)
                        bot.send_message(int(user_id), msg.message)

                    #print('2', doc)
                    print(doc)
                    # file_url = bot.get_file_url(msg.media.document.id)


                    # bot.send_message(int(user_id), msg)
                else:
                    print(f"#сообщение пользователю пользователю {user_id} {entity.title} {entity.id}")
                    bot.send_message(int(user_id), text=msg.message)

            pass
        else:
            async for msg in client.iter_messages(entity, reverse=True, offset_date=datetime.date.today() - datetime.timedelta(hours=1)):
                if not msg.message:
                    continue
                for user in users:
                    isMsg = getUserMessage(user[0], entity.id, msg.id)
                    if not isMsg:
                        doc = await client.download_media(msg)
                        print(f"#файл пользователю {user_id} {entity.title} {entity.id}")
                        if msg.media:
                            print(f"#файл пользователю {user[0]} {entity.title} {entity.id}")
                            bot.send_document(int(user[0]), caption=msg.message, document=doc)
                        else:
                            print(f"#сообщение пользователю пользователю {user[0]} {entity.title} {entity.id}")
                            bot.send_message(int(user[0]), text=msg.message)
                        addNessage(user[0], entity.id, entity.title, msg.id)

def shedulet():
    bot.polling()

def asrun():
    asyncio.run(getMessages(0, 0))
conn = engine.connect()
metadata.create_all(conn)
conn.close()
threading.Thread(target=shedulet).start()
loop1 = asyncio.get_event_loop()
client = TelegramClient('+380930632697', "13973940", "85ad584860e80c93e79d13a4f1632bfb")
client.start()
schedule.every(55).minutes.do(asrun)

print("#BOT IS ONLINE")
while True:
    schedule.run_pending()
    time.sleep(1)
