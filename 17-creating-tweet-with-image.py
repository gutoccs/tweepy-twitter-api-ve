# Responder un tweet

import tweepy
import config

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

# La longitud de media_ids debe ser entre 1 y 4
response = client.create_tweet(text='Hello', media_ids=[1593806455295156224])


print(response)