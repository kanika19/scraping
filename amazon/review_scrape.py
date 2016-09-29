# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:32:41 2015

@author: shubham
"""

from bs4 import BeautifulSoup

from urllib2 import urlopen

BASE_URL = 'http://www.amazon.in/Apple-iPhone-5s-Gold-32GB/dp/B00FXLCLTO/ref=sr_1_1?s=electronics&ie=UTF8&qid=1436160688&sr=1-1&keywords=iphone+5s+32gb'

#html = urlopen(BASE_URL).read()
#soup = BeautifulSoup(html,'lxml')
#review = soup.find('div','a-row')

from pprint import pprint
#from bs4 import BeautifulSoup
import requests

url = 'http://www.amazon.in/Apple-iPhone-5s-Gold-32GB/dp/B00FXLCLTO/'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.content, 'lxml')
tags = {}
for li in soup.select('table#productDetailsTable div.content ul li'):
    print li
    try:
        title = li.b
        key = title.text.strip().rstrip(':')
        value = title.next_sibling.strip()

        tags[key] = value
    except AttributeError:
        break

pprint(tags)