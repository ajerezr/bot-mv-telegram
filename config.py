# -*- coding: utf-8 -*-
import configparser
import os
import sys
import string
import random


# Inicialize settings
ini = 'settings.ini'
Config = configparser.ConfigParser()
errors = {'readini': '\033[31m Error \033[39m - cannot read -> \033[32m {} \033[39m'.format(ini),
    'token': '\033[31m Error - Not Token - \033[39m pls insert token in -> \033[32m {} \033[39m'.format(ini)}

if not Config.read(ini):
    print(errors['readini'])
    sys.exit(1)
if not Config.get('telebot', 'token'):
    print(errors['token'])
    sys.exit(1)
try:
    Temp_folder, Log_folder = Config.get('folders', 'temp_folder'), Config.get('folders', 'log_folder')
    if not os.path.isdir(Temp_folder):
        os.makedirs(Temp_folder)
    if not os.path.isdir(Log_folder):
        os.makedirs(Log_folder)
except Exception as e:
    print(e)
    sys.exit(1)


def getToken():
    return Config.get('telebot', 'token')

def getWheatApiKey():
    return Config.get('apis', 'OpenWheatKey')

def getDomainKey():
    return Config.get('apis', 'DomainKey')

def getTempFolder():
    return Config.get('folders' ,'temp_folder')

def getAdminEmail():
    return Config.get('admin', 'email')

def edit_admin_password():
    #For next dlc
    pass

def edit_admin_email():
    #For next dlc
    pass

def set_logconf_folder(folder):
    log_conf = 'log_config.ini'
    Config = configparser.ConfigParser()
    Config.read(log_conf)
    Config.set('handler_fileHandler','args','("{}loggin.log",)'.format(folder))
    with open(log_conf, 'w') as configfile:
        Config.write(configfile)

# http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def check_admin_key():
    try:
        Config.read(ini)
        set_logconf_folder(Log_folder)
        if not Config.get('admin','key'):
            Config.set('admin', 'key', id_generator())
            with open(ini, 'w') as configfile:
                Config.write(configfile)
            print('You default admin key is: {} - edit {} to change it'.format(Config.get('admin','key'), ini))
    except Exception as error:
        print(error)
        sys.exit(1)
