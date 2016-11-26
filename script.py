import urllib.request
import bs4
import xml.etree.ElementTree as ElementTree


opener = urllib.request.FancyURLopener({})
url = "page.html"
f = opener.open(url)
content = f.read()


tree = ElementTree.fromstring(content)
root = tree.getroot()
