#!/usr/bin/env python3
import configuration as c
import tweepy
from textblob import TextBlob
import time

# Authenticate through twitter
auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
auth.set_access_token(c.access_token, c.access_token_secret)
api = tweepy.API(auth)

# Run the script every 5 seconds and write to a file
for i in range(156):
    # Search for tweets
    public_tweets = api.search('North Korea' or 'NorthKorea' or 'Kim Jong-un' or 'Kim Jong un' or 'nuclear war')

    # Determines the total sentiment analysis score of the all the tweets + logic
    sum_polarity = 0
    num_tweets = 0
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text).sentiment.polarity
        if analysis >= 0.4 or analysis == 0.0:
            analysis = 1.0
        sum_polarity += analysis
        num_tweets += 1

    # Calculates the % chance of a nuke being launched
    SA_value = sum_polarity / num_tweets
    percent_chance = str(round((100 - ((SA_value + 1) * 50)) / 2, 2))

    # Writes % chance to nuke_checker.csv
    save_file = open('nuke_checker.csv', 'a')
    save_file.write(percent_chance)
    save_file.write('\n')
    save_file.close()
    time.sleep(5)
