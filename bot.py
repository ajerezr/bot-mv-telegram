# -*- coding: utf-8 -*-

import telebot, time, config, os, tempfile, subprocess, random, requests, time
from telebot import types
from telebot import util
from random import randint

bot = telebot.TeleBot(config.token())

#############################################
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
        print(mensaje)


bot.set_update_listener(listener)
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################


#############################################
# text
@bot.message_handler(commands=['windows'])
def command_windows(m):
    cid = m.chat.id
    bot.send_message( cid, 'Vete a la mierda')

@bot.message_handler(commands=['hilo'])
def command_hilo(m):
    cid = m.chat.id
    # bot.send_message_with_markdown( cid, "[Hilo GNU/Linux](https://www.mediavida.com/foro/hard-soft/gnulinux-hilo-general-489974)")
    text = "[Hilo GNU/Linux](https://www.mediavida.com/foro/hard-soft/gnulinux-hilo-general-489974)"
    bot.send_message( cid, text, parse_mode="Markdown")

@bot.message_handler(commands=['repo'])
def command_repo(m):
    cid = m.chat.id
    bot.send_message( cid, '[Repositorio en Github](https://github.com/ajerezr/bot-mv-telegram)', parse_mode="Markdown")

@bot.message_handler(commands=['tits'])
def command_tits(m):
    cid = m.chat.id
    rtits = requests.get(r'https://www.reddit.com/r/legalteens+nipples+gonewild+nsfw+nsfw_gif+tits+realgirls/.json')
    number = randint(0,24)
    tits = rtits.json()['data']['children'][number]['data']['url']
    bot.send_message(cid, tits)

@bot.message_handler(commands=['wallpapers'])
def command_wallpapers(m):
    cid = m.chat.id
    r = requests.get(r'https://www.reddit.com/r/wallpapers/.json')
    number = randint(0,20)
    wallpapers = r.json()['data']['children'][number]['data']['url']
    bot.send_message(cid, wallpapers)

#############################################
# peticion
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.

# reddit

