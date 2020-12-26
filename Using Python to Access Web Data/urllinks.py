# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Cillian.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
repeats = soup('a')
out = 0

for repeat in repeats:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    link = 0
    for tag in tags:
        #print(tag.get('href', None))
        url = tag.get('href', None)
        link = link + 1
        if link == 18:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            break
    print(url) 
    out = out + 1
    repeats = soup('a')

    if out == 7:
        break
    

