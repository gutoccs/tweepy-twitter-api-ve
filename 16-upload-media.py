'''
    Carga una imagen en Twitter, sin embargo, esto no genera un tweet
    Cuando se reaiza un tweet de forma manual e indicamos la imagen, esta se carga en background
    porque twitter necesita primero cargarla, luego obtener su ID y mandarlo con el tweet

    Por ahora, la versión 2 del APi de Twitter no tiene un endpoint para carga archivos multimedia,
    por ello se utiliza la versión 1.1
    https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map
'''

import tweepy
import config

# autorización con consumer key y consumer secret
auth = tweepy.OAuthHandler(consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET)

# configurar el acceso al usuario con access key y access secret
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# llamando a la API
api = tweepy.API(auth)

# nombre del archivo, debe estar en el mismo directorio de este archivo
filename = "a.jpg"

# subiendo el archivo
media = api.media_upload(filename)

# imprimiendo la respuesta
print("The media ID is : " + media.media_id_string) # Este valor es muy importante
print("The size of the file is : " + str(media.size) + " bytes")

# 1593806455295156224
