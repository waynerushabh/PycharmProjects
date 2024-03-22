import requests

r=requests.get("https://www.nareshit.com")
r.text
print(r.text)