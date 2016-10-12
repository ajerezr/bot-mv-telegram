from modules.tools import GetJson


def Imdb(message):
    m = ''
    query = 'http://www.omdbapi.com/?t='
    text1 = message.text.strip('/imdb ')
    query += text1.replace(" ", "+")
    query += '&y=&plot=short&r=json'
    info = GetJson(query)
    try:
        title = info['Title'] + '\n'
        year = info['Year'] + '\n'
        rated = info['Rated'] + '\n'
        released = info['Released'] + '\n'
        runtime = info['Runtime'] + '\n'
        director = info['Director'] + '\n'
        writer = info['Writer'] + '\n'
        actors = info['Actors'] + '\n'
        plot = info['Plot'] + '\n'
        poster = info['Poster']
        m = m + '*Title:* ' + '[' + title + ']' + '(' + poster + ')' + '\n' + '*Year:* ' + year +\
               '*Rated:* ' + rated + '*Released:* ' + released + '*Runtime:* ' + runtime + '*Director:* ' +\
               director + '*Writer:* ' + writer + '*Actors:* ' + actors + '*Plot:* ' + plot
        return m
    except KeyError:
        return 'Nope :('
