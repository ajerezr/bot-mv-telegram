# -*- coding: utf-8 -*-

# Set your current API Token here. Obtain your token by creating a bot in: telegram.me/BotFather
TOKEN = ""

# Set your current Api key from api.openwheatermap for run wheater module
# Insert key or None for disable this module
OpenWheatKey = ""

# DomainChecker api key
DomainKey = ""


def getToken():
    return TOKEN


def getWheatApiKey():
    return OpenWheatKey


def getDomainKey():
    return DomainKey
