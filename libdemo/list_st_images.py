from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, 'html.parser')

for img_tag in bs.find_all("img"):
    print(img_tag['src'])
