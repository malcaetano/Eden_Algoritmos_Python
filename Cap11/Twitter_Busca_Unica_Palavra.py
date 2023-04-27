import tweepy
from unidecode import unidecode

consumer_key = 'coloque seu codigo aqui'
consumer_secret = 'coloque seu codigo aqui'
access_token = 'coloque seu codigo aqui'
access_token_secret = 'coloque seu codigo aqui'


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
                       
