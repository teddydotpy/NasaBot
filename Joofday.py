import requests

class Joofday:
    def __init__(self):
        self.url = 'https://icanhazdadjoke.com/'
        self.headers = {'Accept': 'application/json'}
        self.req = requests.get(self.url, headers=self.headers)


    def TwitterSend(self, api):
        data = self.req.text
        message = 'Joke of the day: \n' + data.text['joke']
        api = api
        
        api.update_status(message)
        print(data)
        return 
