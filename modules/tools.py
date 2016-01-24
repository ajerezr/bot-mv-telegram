import requests

def GetJson(url, param=None):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        rest = requests.get(url, params=param, headers=headers)
        return rest.json()
    except requests.exceptions.RequestException:
        return "requests error"

def GetHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    try:
        html = requests.get(url, headers=headers)
        return html
    except requests.exceptions.RequestException:
        return "requests error"

def ChatUserName(m):
    cid = m.chat.id
    if cid > 0:
        return m.chat.first_name
    else:
        return m.from_user.first_name
