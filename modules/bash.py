from bs4 import BeautifulSoup as bs
from modules.tools import GetHtml


def Bash(m):
    ss64 = "http://ss64.com/bash/"
    text = m.text.split(" ")
    if len(text) > 1 and text[1] != "/":
        ss = ss64 + text[1] + ".html"
        r = GetHtml(ss)
        des = bs(r.text, "html.parser").find("p").text
        if "404" in des:
            return "Mala consulta"
        else:
            msg = '[%s](%s)\n' % (text[1], ss) + des
            return msg
    else:
        return "example: /bash echo"
