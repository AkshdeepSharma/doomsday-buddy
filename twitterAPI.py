#!/usr/bin/env python3
import configuration as c
import tweepy
from textblob import TextBlob

# Authenticate through twitter
auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
auth.set_access_token(c.access_token, c.access_token_secret)
api = tweepy.API(auth)

# Search for tweets
public_tweets = api.search('North Korea' or 'NorthKorea' or 'Kim Jong-un' or 'Kim Jong un' or 'nuclear war')

# Determines the total sentiment analysis score of the all the tweets
sum_polarity = 0
num_tweets = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    sum_polarity += analysis.sentiment.polarity
    num_tweets += 1

# Calculates the % chance of a nuke being launched
SA_value = sum_polarity / num_tweets
percent_chance = str(round(100 - (((SA_value + 1) / 2) * 100), 2))
