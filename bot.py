# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import config

bot = telebot.TeleBot(config.token())

#############################################
# log

# def listener(messages):
#     for m in messages:
#         cid = m.chat.id
#         if cid > 0:
#             mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
#         else:
#             mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text
#         f = open( 'files/log', 'a')
#         f.write(mensaje + "\n")
#         f.close()
#         print(mensaje)


# bot.set_update_listener(listener)

#############################################
# text
@bot.message_handler(commands=['windows'])
def command_windows(m):
    cid = m.chat.id
    bot.send_message( cid, 'Vete a la mierda')

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