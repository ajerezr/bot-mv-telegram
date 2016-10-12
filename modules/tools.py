import requests
import unicodedata


def GetJson(url, param=None, queue=None):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        rest = requests.get(url, params=param, headers=headers)
        if queue is not None:
            queue.put(rest.json())
        else:
            return rest.json()
    except requests.exceptions.RequestException:
        return "request error"


def GetHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        html = requests.get(url, headers=headers)
        return html
    except requests.exceptions.RequestException:
        return "request error"


def ChatUserName(m):
    cid = m.chat.id
    if cid > 0:
        return m.chat.first_name
    else:
        return m.from_user.first_name


def Strip_accents(s):
    # http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
