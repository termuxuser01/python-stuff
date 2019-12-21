import requests
from requests.exceptions import HTTPError

resp = requests.get("http://www.example.com")
print(resp)
# get status code
print(resp.status_code)

# check to see if website is up
if resp.status_code == 200:
  print("success!")
elif resp.status_code == 404:
  print("not found")
else: 
  print("unknown")

# if you get a good http response requests will return true, otherwise it will be false if you get a status code between 200 and 400
print(bool(resp))

# raise an exception if request was unsuccesfull
try:
  resp = requests.get("http://www.dsafsdkjladsjf.com/")
  resp.raise_for_status()
except HTTPError as httper:
  print("there has been an http error: {}".format(httper))
except Exception as err:
  print(f'there has been an error : {err}')

# view payload
# in bytes
resp = requests.get("http://www.example.com")
print(resp.content[1:50])
# as string
print(resp.text[1:100])
# apply specific encoding
resp.encoding = 'utf-8'
# return a .json dictionary
# print(resp.json())
print(resp.headers)
# this is dictionary type object so you can use keys
print(resp.headers["Last-Modified"])
