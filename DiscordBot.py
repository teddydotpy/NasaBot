#! /usr/bin/env python3
import GetApod
import requests, datetime, time, random, os
from discord import Webhook, RequestsWebhookAdapter

env = os.environ
Apod = GetApod.Apod()
message = Apod.DiscordSend()
ifApodSent = False
# manyMessages = Apod.MassApods('2020-08-09', '2020-09-15')

webhook = Webhook.from_url(env['WebHookURL'], adapter=RequestsWebhookAdapter())
def get_random_message():
    message = list(open('Messagelist.txt', 'r'))
    return message[random.randrange((len(message)))]

while(True):
    if datetime.datetime.now().time().hour == 10 and not ifApodSent:
        webhook.send(message)
        ifApodSent = True
    elif datetime.datetime.now().time().hour == random.randrange(23):
        webhook.send(get_random_message())
    time.sleep(900)