import tweepy
from unidecode import unidecode
import re


consumer_key = 'coloque seu codigo aqui'
consumer_secret = 'coloque seu codigo aqui'
access_token = 'coloque seu codigo aqui'
access_token_secret = 'coloque seu codigo aqui'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
klist=['Futebol']
public_tweets1 = api.search(klist[0],count=5,result_type='popular')
for tweet in public_tweets1:
          textPort=unidecode(tweet.text)
          processed_text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet.text)
          processed_text = re.sub(r"^RT[\s]+", "", processed_text)
          processed_text = " ".join(processed_text.split())
          processed_text = processed_text.lower()
          print(processed_text)
          print('-------------------------------------------------')
                       
