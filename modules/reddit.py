from modules.tools import get_logger
from modules.tools import GetJson
import threading
import queue

porn_dict = dict()
lock = threading.Lock()
logger = get_logger()

def Reddits(key):
    global porn_dict # un poco guarrete...
    if key in porn_dict.keys():
        try:
            lock.acquire()
            logger.info(porn_dict[key])
            content = porn_dict[key].pop()['data']['url']
            lock.release()
            return content
        except IndexError as indexError: # lista vacia
            logger.warning(indexError)
            lock.release()

    q = queue.Queue()
    r = 'https://www.reddit.com'
    reddits = {'asians_gif': '/r/asian_gifs/.json?limit=100', 'anal': '/r/anal/.json?limit=100',
               'asianhotties': '/r/asianhotties/.json?limit=100', 'AsiansGoneWild': '/r/AsiansGoneWild/.json?limit=100',
               'RealGirls': '/r/RealGirls/.json?limit=100', 'wallpapers': '/r/wallpapers/.json?limit=100',
               'fitnessgirls': ['/r/JustFitnessGirls/.json?limit=100','/r/HotForFitness/.json?limit=100']}
    urls = []
    if key in reddits.keys():
        if isinstance(reddits[key], str):
            urls.append(r + reddits[key])
        else:
            for url in reddits[key]:
                urls.append(r + url)

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
        porn_dict[key] = data
        content = porn_dict[key].pop()['data']['url']
        lock.release()
        return content
    except Exception as e:
        lock.release()
        logger.error(e)
        return "An error ocurred :(", e
