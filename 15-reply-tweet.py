# Responder un tweet

import tweepy
import config

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

response = client.create_tweet(in_reply_to_tweet_id=1590948899954499584, text='Hello')


print(response)