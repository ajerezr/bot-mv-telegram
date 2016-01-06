# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import token

TOKEN = token.t()

bot = telebot.TeleBot(TOKEN)

# log
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if cid > 0:
            print str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
        else:
            print str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text

bot.set_update_listener(listener)
#############################################
# text
@bot.message_handler(commands=['windows'])
def command_windows(m):
    cid = m.chat.id
    bot.send_message( cid, 'Vete a la mierda')

@bot.message_handler(commands=['prueba'])
def command_prueba(m):
    cid = m.chat.id
    bot.send_message( cid, 'log work')

@bot.message_handler(commands=['hilo'])
def command_hilo(m):
    cid = m.chat.id
    bot.send_message( cid, 'Hilo GNU/Linux\n https://www.mediavida.com/foro/hard-soft/gnulinux-hilo-general-489974')

@bot.message_handler(commands=['repo'])
def command_repo(m):
    cid = m.chat.id
    bot.send_message( cid, 'Repositorio en Github\n https://github.com/ajerezr/bot-mv-telegram')

#############################################
# peticion
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.