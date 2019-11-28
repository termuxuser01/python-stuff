import random
import urllib.request

UA_lst = [#place list here
]

url = 'http://httpbin.org/user-agent'

#eg make 5 requests
for i in range(1,6):
    UA = random.choice(UA_lst)
    header = {'User-Agent': UA}
    req = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(req)
    html = resp.read()
