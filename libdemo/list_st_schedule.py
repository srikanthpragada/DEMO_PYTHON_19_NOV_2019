from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, 'html.parser')

schedule_table = bs.find("table",{'id': 'ctl00_ContentPlaceHolder1_GridView2'})
for batch in schedule_table.find_all("tr")[1:]:
       details = batch.find_all("td")
       print(f"{details[0].text:30} {details[2].text:10}  {details[1].text}")