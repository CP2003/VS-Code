import os
import telebot
from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/start ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Welcome to humenbot".format(cmd)

    app.send_message(chat_dest, msg)

@app.route('/help ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "No help page is found !".format(cmd)

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   reply_to = message['text']

   msg = " ⭕⭕⭕ {} ⭕⭕⭕".format(reply_to)
   app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '2034497572:AAFAkRFxFAqmZh0CWgcW_1FDNnFs82iI7KA'
    app.poll(debug=True)