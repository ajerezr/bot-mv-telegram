# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import token

bot = telebot.TeleBot(token.t())
usuarios = [line.rstrip('\n') for line in open('files/usuarios')]

# log

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if cid > 0:
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
        else:
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
        f = open( 'files/log', 'a') 
        f.write(mensaje + "\n")
        f.close()
        print mensaje


bot.set_update_listener(listener)

######################
# Control de usuarios

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if not str(cid) in usuarios:
        usuarios.append(str(cid))
        aux = open( 'files/usuarios', 'a')
        aux.write( str(cid) + "\n")
        aux.close()
        bot.send_message( cid, "Bienvenido!")

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