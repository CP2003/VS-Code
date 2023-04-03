import sys
import time
import telepot
from telepot.loop import MessageLoop
import pdb
from functools import wraps


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg["text"].lower() == "whatsapp":
     
        
        # send the pdf doc
        bot.sendDocument(chat_id=chat_id, document='t.me/fouadupdater/6')
        
        
        
    elif content_type == 'text':
        bot.sendMessage(chat_id, "sorry, I can only deliver news")

# replace XXXX.. with your token
TOKEN = '2034497572:AAFAkRFxFAqmZh0CWgcW_1FDNnFs82iI7KA'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)