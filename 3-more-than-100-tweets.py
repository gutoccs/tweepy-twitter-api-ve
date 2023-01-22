# El código base es lo que se hizo en el punto 1, pero sin comentarios
# La idea es traer se más de 100 tweets, para ello hay que usar un paginador
# Más info sobre el paginador y datos a traer: https://stackoverflow.com/questions/72016766/tweepy-only-lets-me-get-100-results-how-do-i-get-more-ive-read-about-paginati

import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'vinotinto OR leones del caracas -is:retweet -has:media'

'''
max_result debe ser un valor entre 10 y 100
    response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'])  
    
Cómo no se puede más de 100 se creará entonces un paginador con un límite de 1000 tweets 
'''
# Indicamos que por cada llamada se traiga máximo 100 tweets
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    print(tweet.id)
    print(tweet.text)


