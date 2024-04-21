import json
import requests

keyword = input("enter keyword")
request = "https://api.tvmazecom/search/shows?q=" + keyword
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print("request could not be completed.")
