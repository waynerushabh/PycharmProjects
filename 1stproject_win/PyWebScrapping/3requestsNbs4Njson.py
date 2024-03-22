import requests
from bs4 import BeautifulSoup
import csv
import json

r=requests.get("https://www.instahyre.com/job-115916-backend-python-developer-at-tata-consultancy-services-mumbai/")

soup=BeautifulSoup(r.text,'lxml')

f=json.dumps(soup.title.text)
with open('JSONfile1.txt','wt') as outfile:
    json.dump(f, outfile)