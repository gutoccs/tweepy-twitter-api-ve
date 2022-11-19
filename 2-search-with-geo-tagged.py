# El código base es lo que se hizo en el punto 1, pero sin comentarios
# Aquí lo que hicimos fue en búsqueda reciente traernos la ubicación

# Colocaré el código, sin embargo, esta característica está para Cuentas de Nivel Académica

import tweepy
import config

# Usando las credenciales de cuenta académica
client = tweepy.Client(bearer_token=config.ACADEMIC_BEARER_TOKEN)

# place_country:US Indica el país de búsqueda
query = 'vinotinto OR leones del caracas -is:retweet -has:media place_country:US'

# expansions=['geo_place_id'] Traerá metadato sobre la unicación del tweet
response = client.search_recent_tweets(query=query, max_results=30, tweet_fields=['created_at', 'lang'], expansions=['geo_place_id'])

# Se crea el diccionario en base a la ubicación
places = {p['id']: p for p in response.includes['places']}

for tweet in response.data:
    if places[tweet.geo['place_id']]:
        place = places[tweet.geo['place_id']]
        print(tweet.id)
        print(place.full_name) # Imprimirá algo como: Chicago, IL
