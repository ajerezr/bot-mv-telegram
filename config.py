# -*- coding: utf-8 -*-
import configparser
import os
import sys
import traceback
from modules.tools import id_generator

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

def editAdminPassword():
    #For next dlc
    pass

def editAdminEmail():
    #For next dlc
    pass

def configLogFolder(folder):
    log_conf = 'log_config.ini'
    Config = configparser.ConfigParser()
    Config.read(log_conf)
    Config.set('handler_fileHandler','args','("{}loggin.log",)'.format(folder))
    with open(log_conf, 'w') as configfile:
        Config.write(configfile)


if __name__ == '__main__':
    try:
        if not Config.get('admin','key'):
            Config.set('admin', 'key', id_generator())
            with open(ini, 'w') as configfile:
                Config.write(configfile)
            print('You default admin key is: {} - edit {} to change it'.format(Config.get('admin','key'), ini))
        Temp_folder, Log_folder = Config.get('folders', 'temp_folder'), Config.get('folders', 'log_folder')
        if not os.path.isdir(Temp_folder):
            os.makedirs(Temp_folder)
        if not os.path.isdir(Log_folder):
            os.makedirs(Log_folder)
        configLogFolder(Log_folder)
    except Exception as error:
        print(error)
        sys.exit(1)
