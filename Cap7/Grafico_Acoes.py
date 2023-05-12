import pandas as pd
import numpy as np
import matplotlib.pyplot as fig
import pandas_datareader.data as web
import datetime as dt

################ importar a acao ############################
inicio=dt.datetime(2021,1,2)
fim=dt.datetime(2021,11,11)

df=web.DataReader(['PETR4.SA','CL=F'],'yahoo',inicio,fim)['Close']
df['mv5']=df['PETR4.SA'].rolling(window=5).mean()
df.dropna(inplace=True)

figura,ax=fig.subplots(nrows=2,ncols=1)

ax[0]=df.plot(y=['PETR4.SA','mv5'],style=['-','--'],color='black',ax=ax[0])
ax[0].set_ylabel('Preços em reais da Petrobras - PETR4')
ax[1]=df.plot(y='CL=F',style='o-',color='black',ax=ax[1])
ax[1].set_ylabel('Preços do petróleo em dolar')