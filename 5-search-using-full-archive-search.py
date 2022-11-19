# Búsqueda de archivo completo, solo es disponible para cuentas académicas
# De igual manera dejaré el código

import tweepy
import config

# Usando las credenciales de cuenta académica
client = tweepy.Client(bearer_token=config.ACADEMIC_BEARER_TOKEN)

query = 'vinotinto OR leones del caracas -is:retweet'

file_name = 'tweets.txt'

# Especificando fecha de inicio y de fin
# AL ser cuenta académica se tiene acceso a tweets que sobrepasan los 7 días de publicación
start_time = '2020-01-01T00:00:00Z'

end_time = '2020-05-01T00:00:00Z'

response = client.search_all_tweets(query=query, max_result=100, start_time=start_time, end_time=end_time)

for tweet in response.data:
    print(tweet.id)