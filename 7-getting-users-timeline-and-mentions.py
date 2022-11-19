# Obtiene el timeline y menciones de un usuario

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

print('TIMELINE')

# Obtengo el timeline de un usuario
# El id es el ID del usuario dentro de twitter
# tweet_fields=[ 'lang'] Obtiene el idioma del tweet
tweets = client.get_users_tweets(id=225107284, tweet_fields=['lang'])

for tweet in tweets.data:
    print(tweet.id)
    print(tweet.lang)

print('MENCIONES')

# Obtengo las menciones de un usuario

tweets = client.get_users_mentions(id=225107284, tweet_fields=['lang'])

for tweet in tweets.data:
    print(tweet.id)
    print(tweet.lang)

