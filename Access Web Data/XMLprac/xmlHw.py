import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 
import xml.etree.ElementTree as ET



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()

newString = html.decode()

tree = ET.fromstring(newString)

counter = 0 
sum = 0 
counts = tree.findall('.//count')

for count in counts:
    sum += int(count.text)

print("Counter:", counter)
print("Sum:", sum)