#lets learn how to retrieve web pages before we can even think of parsing them
import urllib.request, urllib.parse, urllib.error
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

page=urllib.request.urlopen(input('insert website url: '))
for line in page:
    line=line.decode()
    line=line.strip()
    paragraph=re.findall("^<p>(.+)</p>",line)
    if not len(paragraph)==0:
        print(paragraph)
