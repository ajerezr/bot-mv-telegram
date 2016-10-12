from modules.tools import GetJson


def Urbdict(message):
    try:
        url = 'http://api.urbandictionary.com/v0/define?term=%s' % (message.text.lstrip('/urbdict '))
        data = GetJson(url)
        text = data['list'][0]['definition']
        return text
    except Exception:
        return 'Definition too long :<'
