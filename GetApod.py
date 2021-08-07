import Api, json, requests, os

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
    
    def TwitterSend(self, api):
        data = self.SingleApod()
        title = 'title: ' + data['title'] + '\n'
        description = 'Description: ' + data['explanation'][:20] + '...' + '\n'
        url = 'url:' + str(data['url'])
        image = data['hdurl']
        message = title + description + url

        api = api
        filename = 'temp.jpg'
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            api.update_with_media(filename, status=message)
            os.remove(filename)
            return 
        else:
            print("Unable to download image")
            return message
    

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