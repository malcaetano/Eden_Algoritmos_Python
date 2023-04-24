#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#         Programa apenas para buscar 
#          as hastags mais acessadas
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from textblob import TextBlob as tb
import tweepy
import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as fig

consumer_key = 'MEbEz5ewLzf0lOqg74AdY0GHB'
consumer_secret = 'K2QziIjFVVrl9omjAkno4HXyeC8uEDvvhw4WH9ZOzWKwFMo3QJ'
access_token = '149650363-30wY3uNi340toTtqzO8gFaV5RGL7khOn07t6Q9kh'
access_token_secret = 'zH9RvXiSuQSN5Igrenw11Liyh1mpsekDl0mb5No8Lsv4D'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Brasil = 23424768
#Cidade de São Paulo = 455827
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
api = tweepy.API(auth)
tendencias=api.trends_place(id =23424768,exclude = 'hashtags')
tendBr=json.loads(json.dumps(tendencias,indent=1))
tam=len(tendBr[0]['trends'])
resultado1=pd.Series([])
resultado2=pd.Series([])
i=0
for r in tendBr[0]['trends']:
    resultado1[i] = r['name'].strip('#')
    resultado2[i] = r['tweet_volume']
    i=i+1
#    print(r['name'].strip('#'),'  ',r['tweet_volume'],'  ',r['url'])
data = {'Name':resultado1, 'Vol':resultado2} 
data=pd.DataFrame(data)
x=data.mask(data.eq('None')).dropna()
resTweet=x.sort_values(by=['Vol'],ascending=False)
print(resTweet)

resTweet.plot(kind='bar',x='Name',color='black',rot=30,fontsize=8)

