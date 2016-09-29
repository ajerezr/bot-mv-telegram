import subprocess
import json
from config import getDomainKey

def DomainCheker(x):
    check = "\U00002705"
    nocheck = "\U0000274C"
    msg = {'msg':False, 'status': False,'error': False}
    key = getDomainKey()
    if key:
        if len(x.split(".")) > 2:
            name, dom = x.split(".")[0], x.split(".")[1::]
            tld = ".".join(value for value in dom)
        elif len(x.split(".")) == 2:
            name,tld = x.split(".")
        else:
            msg['msg'] = "Example: 'google.com','becar.co.uk'"
            return msg
        try:
            query = '{"name":"'+name+'","tld":"'+tld+'"}'
            #"curl drama"
            mierda = "curl -X POST --include 'https://domainstatus.p.mashape.com/' -H 'X-Mashape-Key: "+key+"' -H 'Content-Type: application/json' -H 'Accept: application/json' --data-binary '"+query+"'"
            out = repr(subprocess.Popen(mierda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
            rest = json.loads(out[out.find("{")::].replace("'",""))
            if 'error' in rest.keys() or rest['tld_valid'] is False:
                msg['msg'] = "Mala consulta"
                return msg
            else:
                msg['msg'] = "{0} {1} Available".format(rest['domain'], nocheck+" Not" if rest['available'] is False else check)
                return msg
        except Exception as error:
            msg["error"] = error
            return msg
    else:
        msg['status'] = "Module Disable"
        return msg
