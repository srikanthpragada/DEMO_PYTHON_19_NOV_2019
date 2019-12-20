from bs4 import BeautifulSoup
import requests

resp = requests.get("https://www.wired.com/story/best-movies-2019/")
bs = BeautifulSoup(resp.text, 'html.parser')

print("Top 14 movie by wired.com")

for movie in bs.find_all("h2"):
       print(movie.find("em").text)

