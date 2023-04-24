#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     Programa para buscar  palavras-chave no Excel, medir sentimento
#      médio das 
#     Precisa instalar:
#     pip install textblob
#     pip install tweepy
#     pip install python-twitter
#     pip install unidecode
#     pip install googletrans
#     pip install deep-translator
# Se for instalar tweepy direto do site, precisara do "git" que
# devera ser instalado antes usando:
#    conda install git
#    pip install git+https://github.com/tweepy/tweepy.git
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Atencao
#    Nas novas versoes a funcao "api" mudou no "search". Agora
#    devera ser (tem que usar "_tweets):
#    api.search_tweets(nome,count,result_type)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from textblob import TextBlob as tb
import tweepy
import numpy as np
from deep_translator import GoogleTranslator
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
klist=['pão de queijo']
palchv=0
x=np.zeros(1)
public_tweets1 = api.search(klist[0],count=15,result_type='popular')
#Variável que irá armazenar as polaridades
analysis = None
tweets1 = [] # Lista vazia para armazenar scores
for tweet in public_tweets1:
           try:
                       textPort=unidecode(tweet.text)
                       processed_text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet.text)
                       processed_text = re.sub(r"^RT[\s]+", "", processed_text)
                       processed_text = " ".join(processed_text.split())
                       processed_text = processed_text.lower()
                       print(processed_text)
                       print('-------------------------------------------------')
                       textIng=GoogleTranslator(source='auto',target='english').translate(processed_text)
                       analysis = tb(textIng)
                       polarity1 = analysis.sentiment.subjectivity
                       tweets1.append(polarity1)                      
           except:
                   pass
x[palchv]=np.mean(tweets1)
x[np.isnan(x)]=0
print('++++++++++++++++++++++++++++++++++++++++++++')  
print('PALAVRA: ' + str(klist[0]) )                    
print('MÉDIA DE SENTIMENTO: ' + str(x[palchv]))
           
med_geral=np.mean(x)
if med_geral<0.1:
        status='fato'
else:
        status='opinião'
    
print('++++++++++++++++++++++++++++++++++++++++++++')                       
print('MÉDIA GERAL DOS SENTIMENTOS: ' + str(med_geral))
print('STATUS DO SENTIMENTO: ', status)




        




