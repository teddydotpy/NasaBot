#! /usr/bin/env python3
import GetApod
import requests, datetime, time, random, os
import tweepy

env = os.environ
print(env['What'])
# Apod = GetApod.Apod()
# ifApodSent = False
# Today = datetime.datetime.today().day

# #variables for accessing twitter API
# consumer_key = env['twitter_key']
# consumer_secret_key = env['twitter_secret_key']
# access_token = env['twitter_access_token']
# access_secret = env['twitter_access_secret']

# auth = tweepy.AppAuthHandler(consumer_key, consumer_secret_key)
# auth.set_access_token(access_token,access_secret)
# api=tweepy.API(auth)

# api.update_status('Testing 134')
