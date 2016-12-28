import requests
import unicodedata
import logging
import modules.loggers
import telebot
import string
import random

logger = logging.getLogger(__name__)

def GetJson(url, param=None, queue=None):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        rest = requests.get(url, params=param, headers=headers)
        if queue is not None:
            queue.put(rest.json())
            logger.info('Request Done at {}'.format(url))
        else:
            logger.info('Request Done at {}'.format(url))
            return rest.json()
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return "request error"
    except Exception as e:
        logger.error(e)
        return "unknown error"


def GetHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        html = requests.get(url, headers=headers)
        return html
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return "request error"


def ChatUserName(m):
    cid = m.chat.id
    if cid > 0:
        return m.chat.first_name
    else:
        return m.from_user.first_name

# http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
def Strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
