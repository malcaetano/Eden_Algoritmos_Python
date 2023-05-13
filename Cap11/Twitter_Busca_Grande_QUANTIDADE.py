from textblob import TextBlob as tb
import tweepy
import numpy as np
from deep_translator import GoogleTranslator
from unidecode import unidecode
import re
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as fig

consumer_key='pp9Hb1ZwWVNE4K0u9ywYVinlM'
consumer_secret ='aGVHIXFOBU8vHSxKaWew5Gp64WEvzJhqNRgbMFzv9lxsvIKotW'
access_token ='149650363-FNmr7AvPYrjXtx1TOIzeBq74XMLeZ37c9cVGqSYA'
access_token_secret  ='9q4qQwLAVKolbuRAA1AjiRMnsREz0Y76MW8ZfWvx11cGS'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
klist=['futebol']
num_tw = 500
public_tweets1 = tweepy.Cursor(api.search,q=klist[0],result_type='popular').items(num_tw)
pos=0
neg=0
neu=0
polarity1=0
tweets1 = [] # Lista vazia para armazenar scores
pos_list=[]
neg_list=[]
neu_list=[]
for tweet in public_tweets1:
           try:
                       textPort=unidecode(tweet.text)
                       processed_text = re.sub(r"(!?:\@|http?\://|https?\://|www)\S+", "", tweet.text)
                       processed_text = re.sub(r"^RT[\s]+,", "",processed_text)
                       processed_text = " ".join(processed_text.split())
                       processed_text = processed_text.lower()
                       textIng=GoogleTranslator(source='auto',target='english').translate(processed_text)
                       analysis = tb(textIng)
                       polarity1 = analysis.sentiment.polarity
                       tweets1.append(processed_text)
                       if polarity1<0:
                             #neg_list.append(processed_text)   
                             neg=neg+1
                       elif polarity1>0:
                             #pos_list.append(processed_text)   
                             pos=pos+1
                       else:
                             #neu_list.append(processed_text)
                             neu=neu+1
           except:
                   pass
print('++++++++++++++++++++++++++++++++++++++++++++')  
print('TOTAL: ', num_tw )
print('POSITIVOS(%)= ',  100 * round(pos/len(tweets1),3))
print('NEGATIVOS(%)= ', 100 * round(neg/len(tweets1),3))
print('NEUTROS(%)= ', 100 * round(neu/len(tweets1),3))              

twt=" ".join(tweets1)
stopwords = set(STOPWORDS)
stopwords.update(["da", "do","dos","meu", "em", "você", "de", "ao", "os","mas", 
                  "para","sua", "pra", "que", "e", "a", "um", "ser","pela",
                  "uma", "seu", "quem", "o", "pq", "é","sobre","sem","isso",
                  "vai", "vão", "são", "aos", "na", "no", "né","tua","teu",
                  "tá","se","só", "qual", "até", "está", "terá", "lo", "la",
                  "quer","sai","já","ele", "à", "fui","nós", "nosso", "por","brasil",'saúde'])
wordcloud = WordCloud(stopwords=stopwords, background_color='white', 
                      colormap='binary',width=2500, height=2000).generate(twt)     
fig.imshow(wordcloud)
fig.axis('off')

fig.figure()
x=['positivo','negativo','neutro']
y=[pos,neg,neu]
fig.pie(y,explode=(0.2,0.1,0),labels=x,autopct='%1.1f%%')


        




