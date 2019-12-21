import requests

# make custom query strings in urls
# pass params as dictionary
resp = requests.get("https://api.github.com/search/repostories", 
params={'q': 'requests+language:python'})
# pass params as list of tuples
resp = requests.get(  'https://api.github.com/search/repositories',
params=[('q', 'requests+language:python')])
# use simple bytes
requests.get('https://api.github.com/search/repositories',  params=b'q=requests+language:python')

# inspect some attrobutes
resp_json = resp.json()
# print(resp_json)
repostery = resp_json["items"][0]
# print(repostery)
print(f'repostery name: {repostery["name"]}\ndescription: {repostery["description"]}')
