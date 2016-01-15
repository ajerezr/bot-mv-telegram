# -*- coding: utf-8 -*-

import telebot, time, config, os, tempfile, subprocess, random, requests, json, re
from telebot import types
from telebot import util
from random import randint
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot(config.token())

#############################################
# log                                       #
#############################################
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


#bot.set_update_listener(listener)
#############################################
# Handlers                                  #
#############################################
@bot.message_handler(commands=['boobs'])
def boobs(message):
    number = random.randint(1, 3000)
    query = 'http://api.oboobs.ru/boobs/'+str(number)+'/1/rank/'
    r = requests.get(query)
    info = r.json()
    chat_id = message.chat.id
    text = 'http://media.oboobs.ru/boobs/'+info[0]['preview'].strip('boobs_preview/')
    bot.send_message( chat_id, text)

@bot.message_handler(commands=['butts'])
def butts(message):
    number = random.randint(1, 3000)
    query = 'http://api.obutts.ru/butts/'+str(number)+'/1/rank/'
    r = requests.get(query)
    info = r.json()
    chat_id = message.chat.id
    text = 'http://media.obutts.ru/butts/'+info[0]['preview'].strip('butts_preview/')
    bot.send_message( chat_id, text)

@bot.message_handler(commands=['windows'])
def command_windows(m):
    cid = m.chat.id
    bot.send_message( cid, 'Vete a la mierda')

@bot.message_handler(commands=['thread'])
def command_thread(m):
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
    try:
        tits = rtits.json()['data']['children'][number]['data']['url']
        bot.send_message(cid, tits)
    except:
        bot.send_message(cid, "espera chumacho!")

@bot.message_handler(commands=['wallpapers'])
def command_wallpapers(m):
    cid = m.chat.id
    r = requests.get(r'https://www.reddit.com/r/wallpapers/.json')
    number = randint(0,24)
    try:
        wallpapers = rtits.json()['data']['children'][number]['data']['url']
        bot.send_message(cid, wallpapers)
    except:
        bot.send_message(cid, "espera chumacho!")

@bot.message_handler(commands=['bash'])
def command_bash(m):
    ss64 = "http://ss64.com/bash/"
    cid = m.chat.id
    text = m.text.split(" ")
    if len(text) > 1 and text[1]!="/":
        ss = ss64+text[1]+".html"
        r = requests.get(ss)
        des = bs(r.text, "html.parser").find("p").text
        if "404" in des:
            bot.send_message(cid, "Comando desconocido", parse_mode="Markdown")
        else:
            msg = '[%s](%s)\n'%(text[1],ss)+des
            bot.send_message(cid, msg, parse_mode="Markdown")
    else:
        bot.send_message(cid, "example: /bash echo")

@bot.message_handler(commands=['g'])
def command_g(m):
    cid = m.chat.id
    quest = m.text.strip("/g").replace(" ", "+")
    if quest:
        google = "http://www.google.com/search?hl=en&safe=off&q=" + quest[1::]
        r = requests.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s'%(quest[1::]))
        rest = r.json()
        try:
            x2 = rest['responseData']['results'][1]['content']+"\n"+google
            bot.send_message(cid, x2, parse_mode="html", disable_web_page_preview=True)
        except:
            pass
    else:
        bot.send_message(cid, "example: /g cats")

@bot.message_handler(commands=['wiki'])
def command_wiki(m):
    cid = m.chat.id
    quest = m.text.strip("/wiki ")
    if quest:
        baseurl = 'http://es.wikipedia.org/w/api.php'
        my_atts = {}
        my_atts['action'] = 'opensearch'
        my_atts['format'] = 'json'
        my_atts['search'] = quest
        my_atts['limit'] = 1
        resp = requests.get(baseurl, params = my_atts)
        data = resp.json()
        if data[3]:
            url = data[3][0]
            bot.send_message(cid, url)
        else:
            bot.send_message(cid, 'No "hay" resultados de'+quest)
    else:
        bot.send_message(cid, "example: /wiki cats")

#############################################
# peticion
# http://api.oboobs.ru/
#############################################

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
