#! /usr/bin/env python3
from email import message
import GetApod, Joofday
import requests, datetime, time, random, os
import tweepy

env = os.environ
Apod = GetApod.Apod()
Joofday = Joofday.Joofday()
Today = datetime.datetime.today().day

ifApodSent = False
ifJokeSent = False

#variables for accessing twitter API
consumer_key = env.get('twitter_key')
consumer_secret_key = env.get('twitter_secret_key')
access_token = env.get('twitter_access_token')
access_secret = env.get('twitter_access_secret')
movie_list = [
    'bee-movie.txt',
    'Shrek-Script.txt'
]

def get_random_message():
    message = list(open('Messagelist.txt', 'r'))
    return message[random.randrange((len(message)))]

def get_movie_line(movie_script: str) -> str:
    bee_list = list(open(movie_script, 'r'))
    line = random.randrange((len(bee_list)))
    offset = line%16
    return ' '.join(bee_list[line: line + offset])

def movie(movie: list) -> str:
    return movie[random.randrange(len(movie))]

#authenticating to access the twitter API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

while(True):
    if datetime.datetime.now().time().hour == 6 and not ifApodSent:
        Apod.TwitterSend(api)
        ifApodSent = True
    elif datetime.datetime.now().time().hour == random.randrange(23):
        if random.random():
            api.update_status(get_movie_line(movie(movie=movie_list)))
        else:
            api.update_status(get_random_message()) 
        
    elif datetime.datetime.now().time().hour % 3 and not ifJokeSent:
        Joofday.TwitterSend(api)
        ifJokeSent = True


    # Making sure that everythin works at the proper times of day regardless
    # of the time it was started. Pretty neat.   nerd.
    time.sleep(900)
    if Today != datetime.datetime.today().day:
        Today = datetime.datetime.today().day
        ifApodSent = False
        ifJokeSent = False