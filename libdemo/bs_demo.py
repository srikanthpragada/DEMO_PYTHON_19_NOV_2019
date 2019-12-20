from bs4 import BeautifulSoup

st = "<html><body><h1>Title1</h1><h2>Title2.1</h2><h2>Title2.2</h2></body></html>"

bs = BeautifulSoup(st, 'html.parser')

for tag in bs.find_all("h2"):
    print(tag.text)
