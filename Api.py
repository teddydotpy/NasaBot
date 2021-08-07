import requests, json, os
env = os.environ
# This apbstracts away the specific getting of the nasa data stuff.
class ApiRequester:
    def __init__(self):
        self.ApiKey = env['NasaAPI_key']
        self.head = ''

    def ApiGet(self, website):
        data = requests.get(website + self.ApiKey)
        self.head = data.headers
        return data.text

    def ReturnHead(self):
        return self.head