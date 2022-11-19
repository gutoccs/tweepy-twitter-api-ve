# Obtener información sobre un tweet

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# tweet_fields, permite obtener datos a adicionales que no trae la respuesta por default
response = client.get_tweet(id=1580787545650393088, tweet_fields=['created_at'])

tweet = response.data

print(tweet) # Aquí no imprime created_at

print(tweet.created_at)

