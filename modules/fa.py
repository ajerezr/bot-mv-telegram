from modules.tools import GetHtml
from bs4 import BeautifulSoup as bs


def search(query):
    url = 'https://www.filmaffinity.com/es/search.php?stext=%s' % (query.replace(" ", "+").lower())
    html = GetHtml(url).content
    soup = bs(html, "html.parser")
    list_pelis = soup.findAll("div", {"class": "movie-card movie-card-1"})
    msg = []
    if list_pelis:
        for pelis in list_pelis:
            titulo = str(pelis.find('div', {'class': 'mc-title'}).text)
            url = 'https://www.filmaffinity.com' + str(pelis.find('div', {'class': 'mc-title'}).a['href'])
            msg.append((titulo, url))
        return msg
    else:
        return soup


def GetInfoPeli(data):
    # Not Beautiful
    info = {}
    info['Genre'], info['Actors'] = [], []
    try:
        info['Title'] = data.find('title').text.replace(' - FilmAffinity', '').strip()
    except Exception:
        info['Title'] = 'NA'
    try:
        info['Original_title'] = data.find('dl', {'class': 'movie-info'}).dd.text[17:].replace(' aka', '').strip()
    except Exception:
        info['Original_title'] = 'NA'
    try:
        info['Date'] = data.find('dd', {'itemprop': 'datePublished'}).text
    except Exception:
        info['Date'] = 'NA'
    try:
        info['Country'] = data.find('span', {'id': 'country-img'}).img['title']
    except Exception:
        info['Country'] = 'NA'
    try:
        info['Director'] = data.find('span', {'itemprop': 'director'}).span.text
    except Exception:
        info['Director'] = 'NA'
    try:
        info['Guion'] = data.find('dt', text='Guión').findNext('dd').text
    except Exception:
        info['Guion'] = 'NA'
    try:
        info['Music'] = data.find('dt', text='Música').findNext('dd').text
    except Exception:
        info['Music'] = 'NA'
    try:
        info['Sinopsis'] = data.find('dd', {'itemprop': 'description'}).text.replace("(FILMAFFINITY)", "")
    except Exception:
        info['Sinopsis'] = 'NA'
    try:
        info['Image'] = data.find('img', {'itemprop': 'image'})['src']
    except Exception:
        info['Image'] = 'NA'
    try:
        info['Rating'] = data.find('div', {'id': 'movie-rat-avg'})['content']
    except Exception:
        info['Rating'] = 'NA'
    try:
        for items in data.find('dt', text='Reparto').findNext('dd'):
            if str(type(items)) == "<class 'bs4.element.Tag'>":
                info['Actors'].append(items.span.text.strip())
    except Exception:
        info['actors'] = 'NA'
    try:
        for gen in data.findAll('span', {'itemprop': 'genre'}):
            info['Genero'].append(gen.a.text)
    except Exception:
        info['Genero'] = 'NA'
    return info


def FormatMsgInfo(data):
    tags = ['Original_title', 'Date', 'Country', 'Director', 'Guion', 'Music', 'Actors', 'Genero', 'Rating', 'Sinopsis']
    string = "[" + data['Title'] + "](" + data['Image'] + ")" + "\n"
    for tag in tags:
        if type(data[tag]) is list:
            string += "*" + tag + ":* " + data[tag][0]
            for items in range(1, len(data[tag])):
                string += "," + data[tag][items]
            string += "\n"
        else:
            string += "*" + tag + ":* " + data[tag] + "\n"
    return string


def DirectLink(id_url):
    url = 'https://www.filmaffinity.com/es/%s.html' % id_url
    soup = bs(GetHtml(url).content, 'html.parser')
    return soup


def fa_call_back_direct(id_url):
    msg = {}
    d_link_soup = DirectLink(id_url)
    info = GetInfoPeli(d_link_soup)
    msg['info'] = FormatMsgInfo(info)
    return msg


def FiAf(query):
    msg = {'Msg': "", 'error': None}
    result = search(query)
    if type(result) is list:
        msg['list'] = result
    elif 'Búsqueda' in result.title.text:
        msg['Msg'] = "nope :("
    else:
        info = GetInfoPeli(result)
        msg['Msg'] = FormatMsgInfo(info)
    return msg
