#!/usr/bin/python
# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests

r = requests.get("http://msot.bplaced.net/bkp_webprog/links.htm")

data = r.text

soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
        href = link.get('href')
        m = re.search('(http\:\/\/)', href)

# something isn't right?
        print(m.group(0))


