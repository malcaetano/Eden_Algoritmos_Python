import tweepy
from unidecode import unidecode
import re


consumer_key = 'MEbEz5ewLzf0lOqg74AdY0GHB'
consumer_secret = 'K2QziIjFVVrl9omjAkno4HXyeC8uEDvvhw4WH9ZOzWKwFMo3QJ'
access_token = '149650363-30wY3uNi340toTtqzO8gFaV5RGL7khOn07t6Q9kh'
access_token_secret = 'zH9RvXiSuQSN5Igrenw11Liyh1mpsekDl0mb5No8Lsv4D'


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
                       