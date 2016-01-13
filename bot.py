# -*- coding: utf-8 -*-

import telebot, time, config, os, tempfile, subprocess, random, requests, time
from telebot import types
from telebot import util
from random import randint
from bs4 import BeautifulSoup as bs

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

@bot.message_handler(commands=['thread'])
def command_hilo(m):
    cid = m.chat.id
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
    number = randint(0,24)
    wallpapers = r.json()['data']['children'][number]['data']['url']
    bot.send_message(cid, wallpapers)

@bot.message_handler(commands=['bash'])
def command_wallpapers(m):
    ss64 = "http://ss64.com/bash/"
    cid = m.chat.id
    text = m.text.split(" ")
    ss = ss64+text[1]+".html"
    r = requests.get(ss)
    des = bs(r.text, "html.parser").find("p").text
    if "404" in des:
        bot.send_message(cid, "Feck! Comando desconocido", parse_mode="Markdown")
    else:
        msg = '[%s](%s)\n'%(text[1],ss)+des
        bot.send_message(cid, msg, parse_mode="Markdown")



#############################################
# peticion
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.