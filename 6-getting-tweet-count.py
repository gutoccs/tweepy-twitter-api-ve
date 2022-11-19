# Obtener el volumen de tweets para una determinada consulta de búsqueda

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'Miss Venezuela -is:retweet'

# No manda el total sino un arreglo de objetos basado en el tiempo
# Esta ventana de tiempo por defecto es de 15min, con granulatiry indicamos que sea por día
counts = client.get_recent_tweets_count(query=query, granularity='day')


for count in counts.data:
    print(count)