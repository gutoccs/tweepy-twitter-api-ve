# Postear un tweet con solo texto

import tweepy
import config

# Por defecto el bearer token no sirve para generar tweets, esto por el nivel de seguridad

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

response = client.create_tweet(text='Soon!')

print(response)