import urllib3
from bs4 import BeautifulSoup

http=urllib3.PoolManager()
r = http.request('GET','https://www.instahyre.com/job-115916-backend-python-developer-at-tata-consultancy-services-mumbai/')

soup = BeautifulSoup(r.data,'lxml')
print(soup.title)
print(soup.title.text)