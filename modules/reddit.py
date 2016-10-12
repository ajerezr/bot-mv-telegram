from modules.tools import GetJson
import random
import threading
import queue


def Reddits(*keys):
    q = queue.Queue()
    r = 'https://www.reddit.com'
    reddits = {'asians_gif': '/r/asian_gifs/.json?limit=100', 'anal': '/r/anal/.json?limit=100',
               'asianhotties': '/r/asianhotties/.json?limit=100', 'AsiansGoneWild': '/r/AsiansGoneWild/.json?limit=100',
               'RealGirls': '/r/RealGirls/.json?limit=100', 'wallpapers': '/r/wallpapers/.json?limit=100',
               'JustFitnessGirls': '/r/JustFitnessGirls/.json?limit=100',
               'HotForFitness': '/r/HotForFitness/.json?limit=100'}
    urls = []
    for key in keys:
        if key in reddits.keys():
            urls.append(r + reddits[key])
    try:
        threads = []
        for url in urls:
            t = threading.Thread(target=GetJson, args=(url,), kwargs=dict(queue=q))
            threads.append(t)
            t.start()
        data = []
        for thread in threads:
            thread.join()
            result = q.get()
            data.extend(result['data']['children'])
        npost = len(data)
        xpost = random.randint(1, npost)
        content = data[xpost]['data']['url']
        return content
    except KeyError and TypeError and Exception as e:
        return "An error ocurred :(", e
