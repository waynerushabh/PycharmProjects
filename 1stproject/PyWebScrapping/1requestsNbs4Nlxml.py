import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.instahyre.com/job-115916-backend-python-developer-at-tata-consultancy-services-mumbai/")

soup = BeautifulSoup(r.text,'lxml')
print(soup.title)
print(soup.title.text)