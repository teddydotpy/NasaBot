import requests, json

class Joofday:
    def __init__(self):
        self.url = 'https://icanhazdadjoke.com/'
        self.headers = {'Accept': 'application/json'}
        self.req = requests.get(self.url, headers=self.headers)


    def TwitterSend(self, api):
        data = json.loads(self.req.text)
        message = 'Joke of the day: \n' + data['joke']
        api = api
        
        api.update_status(message)
        print(data)
        return 
