#!/usr/bin/env python

# url text dumper using beautifulsoup
# based on bs4 quicksart guide and 
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/ 

import sys
import requests
from bs4 import BeautifulSoup


url=sys.argv[1]

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'})

print(url)

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

print(soup.get_text())
