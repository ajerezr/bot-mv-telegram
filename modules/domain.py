import urllib.request
from urllib.error import HTTPError
import json
from config import getDomainKey
import re


def DomainChecker(x):
    check = "\U00002705"
    nocheck = "\U0000274C"
    fail = "\U0001F4A5"
    msg = {'msg': False, 'status': False, 'error': False}
    key = getDomainKey()
    regex = "(^|[a-zA-Z0-9@]*\s*)(?P<name>[a-zA-Z0-9_-]+)\.(?P<tld>[a-zA-Z0-9\._-]+)\s*$"
    USER_AGENT = "unirest-python/1.1.6"
    if key:
        url = "https://domainstatus.p.mashape.com/"

        match = re.search(regex, x)
        if(match):
            name = match.group('name')
            tld = match.group('tld')
        else:
            msg['msg'] = "Example: 'google.com','becar.co.uk'"
            return msg
        try:
            dict_payload = {"name":name, "tld":tld} 
            payload = json.dumps(dict_payload).encode('utf8')

            req = urllib.request.Request(url, method='POST', data=payload, headers={'content-type' : 'application/json', 'X-Mashape-Key': key, "user-agent" : USER_AGENT})
            response = urllib.request.urlopen(req)
            response_body = response.read()
            rest = json.loads(response_body.decode('utf-8'))
            msg['msg'] = "{0} {1} Available".format(rest['domain'], nocheck + " Not" if rest['available'] is False else check)
        except HTTPError as error: 
            if(error.code < 500):
                msg["error"] = fail + " The API rejected your request (HTTP "+str(error.code)
            else:
                msg["error"] = fail + "API error (HTTP "+str(error.code)
            msg["error"] += ": "+error.reason+")" if error.reason is not "" else ")"
        except Exception as e:
            msg["error"] = e

        return msg
    else:
        msg['status'] = "Module Disabled"
        return msg