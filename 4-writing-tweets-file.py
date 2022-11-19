# El código base es lo que se hizo en el punto 3, pero sin comentarios
# Ahora en cada línea dela archivo colocará el ID del tweet


import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'vinotinto OR leones del caracas -is:retweet -has:media'

# Nombre del archivo
file_name = 'tweets.txt'

# Se crea el archivo y hará un append, es decir, escribir al final del archivo
with open(file_name, 'a+') as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
        # print(tweet.id)
        filehandler.write('%s\n' % tweet.id)


