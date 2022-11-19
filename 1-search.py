# Searching for tweets from last 7 days 
# Por el tipo de cuenta solo buscará en los últimos 7 días

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# Buscará los tweets que contengan la palabra vinotinto o leones del caracas, que no sean retweet ni que contenga archivos multimedia
query = 'vinotinto OR leones del caracas -is:retweet -has:media'

"""
    Esto se encuentra en la documentación en Twitter
    query indica lo que queremos traernos
    max_results la cantidad de tweet que queremos traernos en la petición
    tweet_fields=['created_at', 'lang'] a qué hora los tweets fueron creados y el idioma
    user_fields=['profile_image_url'] solicita en la respuesta la URL de la imagen de perfil del usuario
    expansions=['author_id'] solicita en la respuesta que agreguen el ID del usuario que generó el tweet, esta información NO estara en response.data sino,
                                en response.includes.users... No solo traerá el ID, sino también su nombre y nombre de usuario

    Ojo en la documentación aparecerá fields y expansions por separado, porque describe todas las opciones de cada una
"""
response = client.search_recent_tweets(query=query, max_results=30, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'],  expansions=['author_id'])
 
# Aquí se está creando un diccionario con la información de los usuarios que postean
# El key es el ID del usuario en Twitter y el value toda la info de dicho usuario
users = {u['id']: u for u in response.includes['users']}


print(users)
# data es donde se trae los tweets, la mayoría de los otros campos son metadata
for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id)
        print(user.username)
        print(user.profile_image_url)
