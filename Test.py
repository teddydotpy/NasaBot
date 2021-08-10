#! /usr/bin/env python3
import GetApod
import requests, json

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
req = json.loads(requests.get(url, headers=headers).text)


print(req['joke'])