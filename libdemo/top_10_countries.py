import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code == 200:
   countries = resp.json()
   for c in sorted(countries,key=lambda c: c['population'], reverse=True)[:10]:
       print(f"{c['name']:50} {c['population']:15d} {c['area']:15.0f}")
else:
    print("Sorry! Could not get details of countries!")

