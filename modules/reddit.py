from modules.tools import GetJson
import random
import threading

data = []

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
            if data:
                return data.pop()

            r = GetJson(url)
            for post in r['data']['children']:
                data.append(post['data']['url'])

            return data.pop()
        except KeyError and TypeError and Exception as e:
            return "An error ocurred :(",e