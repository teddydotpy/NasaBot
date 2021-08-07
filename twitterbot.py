#! /usr/bin/env python3
import GetApod
import requests, datetime, time, random, os
import tweepy

env = os.environ
Apod = GetApod.Apod()
ifApodSent = False
Today = datetime.datetime.today().day

#variables for accessing twitter API
consumer_key = env['twitter_key']
consumer_secret_key = env['twitter_secret_key']
access_token = env['twitter_access_token']
access_secret = env['twitter_access_secret']

def get_random_message():
    message = list(open('Messagelist.txt', 'r'))
    return message[random.randrange((len(message)))]

#authenticating to access the twitter API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

Apod.TwitterSend(api)

while(True):
    if datetime.datetime.now().time().hour == 10 and not ifApodSent:
        Apod.TwitterSend(api)
        ifApodSent = True
        print('The message was sent at ' + str(datetime.datetime.now()))
    elif datetime.datetime.now().time().hour == random.randrange(23):
        api.update_status(get_random_message())

    # Making sure that everythin works at the proper times of day regardless
    # of the time it was started. Pretty neat.   
    time.sleep(900)
    if Today != datetime.datetime.today().day:
        Today = datetime.datetime.today().day
        ifApodSent = False