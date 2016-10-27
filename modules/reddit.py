from modules.tools import GetJson
import threading
import queue

porn_dict = dict()
lock = threading.Lock()


def Reddits(*keys):
    global porn_dict # un poco guarrete...
    for key in keys:
        if key in porn_dict.keys():
            try:
                lock.acquire()
                content = porn_dict[key].pop()['data']['url']
                lock.release()
                return content
            except IndexError: # lista vacia
                lock.release()
                break
    q = queue.Queue()
    r = 'https://www.reddit.com'
    reddits = {'asians_gif': '/r/asian_gifs/.json?limit=100', 'anal': '/r/anal/.json?limit=100',
               'asianhotties': '/r/asianhotties/.json?limit=100', 'AsiansGoneWild': '/r/AsiansGoneWild/.json?limit=100',
               'RealGirls': '/r/RealGirls/.json?limit=100', 'wallpapers': '/r/wallpapers/.json?limit=100',
               'JustFitnessGirls': '/r/JustFitnessGirls/.json?limit=100',
               'HotForFitness': '/r/HotForFitness/.json?limit=100'}
    urls = []
    k = None
    for key in keys:
        if key in reddits.keys():
            urls.append(r + reddits[key])
            if k is None:
                k = key
    try:
        threads = []
        for url in urls:
            t = threading.Thread(target=GetJson, args=(url,), kwargs=dict(queue=q))
            threads.append(t)
            t.start()
        data = list()
        for thread in threads:
            thread.join()
            result = q.get()
            data.extend(result['data']['children'])
        lock.acquire()
        porn_dict[k] = data
        content = porn_dict[key].pop()['data']['url']
        lock.release()
        return content
    except Exception as e:
        lock.release()
        return "An error ocurred :(", e
