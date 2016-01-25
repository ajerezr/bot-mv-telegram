from modules.tools import GetJson

def Boobs(number):
    query = 'http://api.oboobs.ru/boobs/'+str(number)+'/1/rank/'
    info = GetJson(query)
    text = 'http://media.oboobs.ru/boobs/'+info[0]['preview'].strip('boobs_preview/')
    return text

def Butts(number):
    query = 'http://api.obutts.ru/butts/'+str(number)+'/1/rank/'
    info = GetJson(query)
    text = 'http://media.obutts.ru/butts/'+info[0]['preview'].strip('butts_preview/')
    return text
