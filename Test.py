#! /usr/bin/env python3
import GetApod
import requests

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
req = requests.get(url, headers=headers)


print(req.text)