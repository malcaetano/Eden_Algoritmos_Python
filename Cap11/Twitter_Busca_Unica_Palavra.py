import tweepy
from unidecode import unidecode

consumer_key='pp9Hb1ZwWVNE4K0u9ywYVinlM'
consumer_secret ='aGVHIXFOBU8vHSxKaWew5Gp64WEvzJhqNRgbMFzv9lxsvIKotW'
access_token ='149650363-FNmr7AvPYrjXtx1TOIzeBq74XMLeZ37c9cVGqSYA'
access_token_secret  ='9q4qQwLAVKolbuRAA1AjiRMnsREz0Y76MW8ZfWvx11cGS'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
klist=['Bolsonaro']
public_tweets1 = api.search(klist[0],count=5,result_type='recent')
for tweet in public_tweets1:
                       textPort=unidecode(tweet.text)
                       print(textPort)
                       print('-------------------------------------------------')
                       