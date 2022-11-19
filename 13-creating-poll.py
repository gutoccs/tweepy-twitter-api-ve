# Creando una encuesta

import tweepy
import config

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

'''
    poll_duration_minutes indica el tiempo de duración de la encuesta en minutos
    poll_options indica las opciones de la encuesta
    
    El número mínimo de opciones es 2 y máximo 4
'''
response = client.create_tweet(text="Poll's example", poll_duration_minutes=60, poll_options=['option a',
                                                                                              'option b',
                                                                                              'option c',
                                                                                              'option d'])

