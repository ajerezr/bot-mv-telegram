from modules.tools import GetHtml
from bs4 import BeautifulSoup as bs

def search(query):
    url = 'https://www.filmaffinity.com/es/search.php?stext=%s' % (query.replace(" ","+").lower())
    html = GetHtml(url).content
    soup = bs(html, "html.parser")
    list_pelis = soup.findAll("div", {"class":"movie-card movie-card-1"})
    msg = []
    if list_pelis:
        for pelis in list_pelis:
            titulo = str(pelis.find('div',{'class':'mc-title'}).text)
            url = 'https://www.filmaffinity.com' + str(pelis.find('div',{'class':'mc-title'}).a['href'])
            msg.append((titulo,url))
        return msg
    else:
        return soup

def FormatList(sl):
    msg = "*Mas de un resultado:*\n"
    for titulo,link in sl:
        msg+="*"+titulo.replace("  ","")+"* \n"+"/fa "+link.replace("https://www.filmaffinity.com/es/","").strip(".html")+"\n"
    return msg

def GetInfoPeli(data):
    info = {}
    info['Title'] = data.find('title').text.replace(' - FilmAffinity','').strip()
    info['Original_title'] = data.find('dl',{'class':'movie-info'}).dd.text[17:].replace(' aka','').strip()
    info['Date'] = data.find('dd',{'itemprop':'datePublished'}).text
    info['Country'] = data.find('span',{'id':'country-img'}).img['title']
    info['Director'] = data.find('span',{'itemprop':'director'}).span.text
    info['Guion'] = data.find('dt',text='Guión').findNext('dd').text
    info['Music'] = data.find('dt',text='Música').findNext('dd').text
    info['Sinopsis'] = data.find('dd',{'itemprop':'description'}).text.replace("(FILMAFFINITY)","")
    info['Image'] = data.find('img',{'itemprop':'image'})['src']
    try:
        info['Rating'] = data.find('div',{'id': 'movie-rat-avg'})['content']
    except:
        info['Rating'] = 'NA'
    info['Genre'],info['Actors'] = [],[]
    for items in data.find('dt',text='Reparto').findNext('dd'):
        if str(type(items)) == "<class 'bs4.element.Tag'>":
            info['Actors'].append(items.span.text.strip())
    for gen in data.findAll('span',{'itemprop':'genre'}):
        info['Genre'].append(gen.a.text)
    return info

def FormatMsgInfo(data):
    tags = ['Original_title','Date','Country','Director','Guion','Music','Actors','Genre','Rating','Sinopsis']
    string = "["+data['Title']+"]("+data['Image']+")"+"\n"
    for tag in tags:
        if type(data[tag]) is list:
            string += "*"+tag+":* "+data[tag][0]
            for items in range (1,len(data[tag])):
                string += ","+data[tag][items]
            string +="\n"
        else:
            string += "*"+tag+":* "+data[tag]+"\n"
    return string

def DirectLink(id_url):
    url = 'https://www.filmaffinity.com/es/%s.html' % (id_url)
    soup = bs(GetHtml(url).content,'html.parser')
    return soup

##########
# "Main" # http://i1.kym-cdn.com/entries/icons/original/000/013/743/Naamloos-2.png
#################################################################
# if query is film"id":'film344554' and "sure" is good id
# return formating info -> FormatMsgInfo(food)
# if query is other string
# shearch this string
# if shearch result is list return this list -> FormatList(food)
# else result is film description then -> FormatMsgInfo(food)
# >shit return "error"
################################################################
def FiAf(query):
    msg = {'Msg':"",'error':None}
    if "film" in query and query.split("film")[1].isdigit():
        id_url = query.split("film")[1] if len(query.split("film")[1]) == 6 else None
        if id_url:
            try:
                d_link_soup = DirectLink(query)
                info = GetInfoPeli(d_link_soup)
                msg['Msg'] = FormatMsgInfo(info)
            except:
                msg['error'] = query+" *Mala consulta*"
        else:
            msg['error'] = query+" *id error*"
    else:
        result = search(query)
        if type(result) is list:
            msg['Msg'] = FormatList(result)
        elif 'Búsqueda' in result.title.text:
            msg['Msg'] = "nope :("
        else:
            info = GetInfoPeli(result)
            msg['Msg'] = FormatMsgInfo(info)
    return msg
