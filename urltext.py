#!/usr/bin/env python

# url text dumper using beautifulsoup
# based on bs4 quicksart guide and 
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/ 

import sys
import requests
from bs4 import BeautifulSoup
import logging
import http.client as http_client
import argparse

parser = argparse.ArgumentParser(description='Print page text of given url')
parser.add_argument('-u', '--url', action="store", nargs=1,
                    help='url for which text is request')
parser.add_argument('-d', '--debug', action='store_true',
                    help='turn on debug of network connection')

args = parser.parse_args()

# add http connection debugging
# https://stackoverflow.com/a/16630836/8928529
if args.debug:
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

url=args.url[0]

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'})

print(url)

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

print(soup.get_text())
