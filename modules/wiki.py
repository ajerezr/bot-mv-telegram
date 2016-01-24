from modules.tools import GetJson

def Wiki(m):
    baseurl = 'http://es.wikipedia.org/w/api.php'
    my_atts = {}
    my_atts['action'] = 'opensearch'
    my_atts['format'] = 'json'
    my_atts['limit'] = 1
    quest = m.text.strip("/wiki ")
    if quest:
        my_atts['search'] = quest
        data = GetJson(baseurl, my_atts)
        try:
            url = data[3][0]
            return url
        except IndexError:
            return "Mala consulta"
    else:
        return "example: /wiki cats"
