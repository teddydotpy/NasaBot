import Api, json

class Apod:
    def __init__(self):
        self.ApiObject = Api.ApiRequester()

    def SingleApod(self):
        website = 'https://api.nasa.gov/planetary/apod?api_key='
        return json.loads(self.ApiObject.ApiGet(website))

    def ManyApod(self, start, end):
        website = 'https://api.nasa.gov/planetary/apod?start_date=' + start + '&end_date=' + end +  '&api_key='
        return json.loads(self.ApiObject.ApiGet(website))

    def DiscordSend(self):
        data = self.SingleApod()
        title = data['title']
        description = data['explanation']
        image = data['hdurl']
        return 'Title: ' + title + '\n' + 'Description: ' + description + '\n' + image

    def MassApods(self, start, end):
        Apods = self.ManyApod(start, end)
        messagelist = []
        for i in Apods:
            messagelist.append(
                i['title'] + '\n' +
                i['explanation'] + '\n' +
                i['url']
            )
        return messagelist 