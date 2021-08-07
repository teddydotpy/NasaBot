#! /usr/bin/env python3
import GetApod
import requests, datetime, time, random, os
from discord import Webhook, RequestsWebhookAdapter

env = os.environ
Apod = GetApod.Apod()
message = Apod.DiscordSend()
ifApodSent = False
Today = datetime.datetime.today().day

def get_random_message():
    message = list(open('Messagelist.txt', 'r'))
    return message[random.randrange((len(message)))]

while(True):
    if datetime.datetime.now().time().hour == 10 and not ifApodSent:
        webhook.send(message)
        ifApodSent = True
        print('The message was sent at ' + str(datetime.datetime.now()))
    elif datetime.datetime.now().time().hour == random.randrange(23):
        webhook.send(get_random_message())


    # Making sure that everythin works at the proper times of day regardless
    # of the time it was started. Pretty neat.   
    time.sleep(900)
    if Today != datetime.datetime.today().day:
        Today = datetime.datetime.today().day
        ifApodSent = False