#lets learn how to scrape websites
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
lyric_list=list()
site=urllib.request.urlopen(input('insert site: '), context=ctx).read()
soup=BeautifulSoup(site,"html.parser")
lyric=soup("br")
lyrics=str(lyric)
print(lyrics)
