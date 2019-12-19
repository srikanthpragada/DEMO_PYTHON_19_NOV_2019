import requests

name = "srikanth_pragada"
resp = requests.get(f"https://api.github.com/users/{name}")
if resp.status_code == 200:
    details = resp.json() # Convert json in response to dict
    print(details['name'])
    print(details['public_repos'])
    print(details['followers'])
else:
    print("Sorry! Could not get details of user!")

