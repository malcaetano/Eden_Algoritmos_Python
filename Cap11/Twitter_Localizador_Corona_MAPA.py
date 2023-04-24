import pandas as pd
import matplotlib.pyplot as fig
import numpy as np
import os

os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap
map = Basemap(width=9000000,height=8000000,projection='lcc',
            resolution=None,lat_1=-20.,lat_2=-20,lat_0=-15,lon_0=-40.)
map.bluemarble()
map.drawparallels(np.arange(-90.,120.,30.),color='white')
map.drawmeridians(np.arange(0.,420.,60.),color='white')

df=pd.read_excel('Res_CORONA.xlsx',sheet_name='Planilha2')
df=df[-28700:]
df.index=range(len(df.index))

x=np.zeros(len(df))
y=np.zeros(len(df))
for i in range(len(df)):
         test_str = df['local'][i]
         res = eval(test_str) 
         x[i]=res[0]
         y[i]=res[1]
         long, lat = map(*zip(*[res]))
         map.plot(long, lat, marker='o', markersize=5, 
                  markerfacecolor='white')

lugar=pd.DataFrame({'lat':y,'long':x})
lugar['data']=df['data']
achou=lugar[lugar['long']==-53.073466888999974]

fig.figure()
################ verificando a longitude mais frequente #################
cont=lugar['long'].value_counts()

cont.plot.pie(autopct='%1.2f')
#########################################################################



