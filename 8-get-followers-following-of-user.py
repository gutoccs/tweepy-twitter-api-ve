# Obteniendo los seguidores y seguidos de una cuenta

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

print('FOLLOWERS')
users = client.get_users_followers(id=225107284, user_fields=['profile_image_url'])

for user in users.data:
    print(user.profile_image_url)

print('FOLLOWING')
users = client.get_users_following(id=225107284, user_fields=['profile_image_url'])

for user in users.data:
    print(user.profile_image_url)