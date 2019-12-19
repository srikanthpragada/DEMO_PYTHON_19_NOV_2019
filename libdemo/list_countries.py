import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code == 200:
   countries = resp.json()
   for c in countries:
       print(f"{c['name']:50} {c['capital']}")
else:
    print("Sorry! Could not get details of countries!")

