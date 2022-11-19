# Obtener los usuarios que hacen retweet de un tweet

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

users = client.get_retweeters(id=1580782945261920256)



# Ojo da un error si no hay retweeters porque users sería un tipo None y este no es iterable
for user in users.data:
    print(user.username)