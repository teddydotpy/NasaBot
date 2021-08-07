#! /usr/bin/env python3
import GetApod
import requests, datetime, time, random, os
from discord import Webhook, RequestsWebhookAdapter

env = os.environ
Apod = GetApod.Apod()
ifApodSent = False
Today = datetime.datetime.today().day
# manyMessages = Apod.MassApods('2020-08-09', '2020-09-15')

webhook = Webhook.from_url(env['WebHookURL'], adapter=RequestsWebhookAdapter())
def get_random_message():
    message = list(open('Messagelist.txt', 'r'))
    return message[random.randrange((len(message)))]

while(True):
    if datetime.datetime.now().time().hour == 10 and not ifApodSent:
        message = Apod.DiscordSend()
        webhook.send(message)
        ifApodSent = True
    elif datetime.datetime.now().time().hour == random.randrange(23):
        webhook.send(get_random_message())


    # Making sure that everythin works at the proper times of day regardless
    # of the time it was started. Pretty neat.   
    time.sleep(900)
    if Today != datetime.datetime.today().day:
        Today = datetime.datetime.today().day
        ifApodSent = False