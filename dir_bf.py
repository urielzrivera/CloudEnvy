import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def isdomainup(domain):
    httpsUrl = "https://"+domain
    httpUrl = "http://"+domain
    urls = []
    try:
        requests.get(httpsUrl+"/robots.txt", timeout=5,verify=False)
        urls.appen(httpsUrl)
    except:
        pass:
    try:
        requests.get(httpUrl+"/robots.txt",timeout=5,verify=False)
        urls.append(httpUrl)
    except:
        pass:
    if urls:
        return urls
    else:
        return False
