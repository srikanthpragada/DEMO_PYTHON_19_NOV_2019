from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'lxml-xml')

for item in bs.find_all("item"):
    pubdate = item.find("pubDate").text
    if '2019' in pubdate:
       title = item.find("title").text.strip()
       print(title)


