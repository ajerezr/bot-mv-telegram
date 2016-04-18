from modules.tools import GetJson
import random
import threading

def Reddits(key):
    r = 'https://www.reddit.com'
    urls = {}
    urls['asians_gif'] = '/r/asian_gifs/.json?limit=100'
    urls['anal'] = '/r/anal/.json?limit=100'
    urls['asianhotties'] = '/r/asianhotties/.json?limit=100'
    urls['AsiansGoneWild'] = '/r/AsiansGoneWild/.json?limit=100'
    urls['RealGirls'] = '/r/RealGirls/.json?limit=100'
    urls['wallpapers'] = '/r/wallpapers/.json?limit=100'
    if key in urls.keys():
        url = r+urls[key]
    try:
        r = GetJson(url)
        npost = len(r['data']['children'])
        xpost = random.randint(1,npost)
        content = r['data']['children'][xpost]['data']['url']
        return content
    except KeyError and TypeError and Exception as e:
        return "An error ocurred :(",e