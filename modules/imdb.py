from modules.tools import GetJson

def Imdb(message):
    pene = ''
    query = 'http://www.omdbapi.com/?t='
    text1 = (message.text).strip('/imdb ')
    query += text1.replace(" ", "+")
    query += '&y=&plot=short&r=json'
    info = GetJson(query)
    try:
        title = info['Title'] + '\n'
        year = info['Year']  + '\n'
        rated = info['Rated'] + '\n'
        released = info['Released'] + '\n'
        runtime = info['Runtime'] + '\n'
        director = info['Director'] + '\n'
        writer = info['Writer']  + '\n'
        actors = info['Actors'] + '\n'
        plot = info['Plot'] + '\n'
        poster = info['Poster']
        pene = pene + '*Title:* ' + '['+title+']'+'('+poster+')' +'\n' + '*Year:* ' +year + '*Rated:* ' + rated + '*Released:* ' + released + '*Runtime:* ' + runtime + '*Director:* ' + director + '*Writer:* ' + writer + '*Actors:* ' + actors + '*Plot:* ' + plot
        return pene
    except KeyError:
        return 'Nope :('
