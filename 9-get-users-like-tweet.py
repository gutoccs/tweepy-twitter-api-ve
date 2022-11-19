# Obteniendo los lista de usuarios a los que les gusta cieto tweet y así obtener una identificación (username)

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# URL de un tweet: https://twitter.com/gutoccs/status/1580787545650393088
# Entonces el ID del tweet es 1580787545650393088

users = client.get_liking_users(id=1580787545650393088)

for user in users.data:
    print(user.username)