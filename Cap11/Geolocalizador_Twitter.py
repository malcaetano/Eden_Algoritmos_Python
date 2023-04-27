import tweepy
import geocoder
import numpy as np
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap

consumer_key = 'coloque seu codigo aqui'
consumer_secret = 'coloque seu codigo aqui'
access_token = 'coloque seu codigo aqui'
access_token_secret = 'coloque seu codigo aqui'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

searchString = "eleição"

cursor = tweepy.Cursor(api.search, q=searchString, count=5000, 
                       lang="pt", tweet_mode='extended',result_type='recent')

maxCount = 20
count = 0
mat=np.zeros((maxCount,2))
list=[]
for tweet in cursor.items():    
    print()
    print("Tweet Information")
    print("================================")
    print("Text: ", tweet.full_text)
    print("Geo: ", tweet.geo)
    print("Coordinates: ", tweet.coordinates)
    print("Place: ", tweet.place)
    print()

    print("User Information")
    print("================================")
    print("Location: ", tweet.user.location)
    print("Geo Enabled? ", tweet.user.geo_enabled)
    result = geocoder.arcgis(tweet.user.location)
    # x = longitude, y = latitude
    tweet.place = (result.x, result.y)
    if tweet.place[0]!=None:
              list.append(tweet.place)
    print(tweet.place)
    count = count + 1
    if count == maxCount:
        break;
#++++++++++++++++ localização no Mapa ++++++++++++++++++++++++++++++++
map = Basemap(projection='merc', llcrnrlat=-45, urcrnrlat=15,
                llcrnrlon=-90, urcrnrlon=-22, resolution='l')
land_color = 'lightgray'
water_color = 'lightblue'

map.fillcontinents(color='white', lake_color=water_color)
map.drawcoastlines()
#++++++++++++++++ desenhando os meridianos ++++++++++++++++++++++++++
map.drawparallels(np.arange(-90.,120.,30.))
map.drawmeridians(np.arange(0.,420.,60.))
map.drawmapboundary(fill_color=water_color)
map.drawcountries(linewidth=2,color='#6D5F47')
#++++++++++++++++ coletando as coordenadas para plotar a localizacao          
long, lat = map(*zip(*list))
#++++++++++++++++ plotando o local das mensagens ++++++++++++++++++++++
map.plot(long, lat, marker='o', markersize=6, markerfacecolor='red', linewidth=0)
