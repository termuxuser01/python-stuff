import urllib.request
# format: User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>

url = 'http://httpbin.org/user-agent'
UA = user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
req = urllib.request.Request(url, headers={'User-Agent': UA})
resp = urllib.request.urlopen(req)
html = resp.read()
print(html)

