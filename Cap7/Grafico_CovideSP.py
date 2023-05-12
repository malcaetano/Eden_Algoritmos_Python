import pandas as pd
import numpy as np
import matplotlib.pyplot as fig

df=pd.read_excel('Covid_SP.xlsx')
df['taxa-hosp']=df['UTImd7dias'].diff()
df.index=df['data']
df=df.drop(['data','UTImd7dias'],axis=1)
df['Caso7d']=df['Casos'].rolling(window=7).mean()
df['Morte7d']=df['Mortes'].rolling(window=7).mean()
df.dropna(inplace=True)
print(df)

figura,ax=fig.subplots(nrows=2,ncols=1)

ax[0]=df.plot(y=['Caso7d'],style=['-'],color='black',linewidth=3,ax=ax[0])
ax[0].set_ylabel('Casos  - Média Móvel de 7 dias',size=15)
ax2=ax[0].twinx()
ax2=df.plot(y='Morte7d',style='o-',color='black',alpha=0.3, ax=ax2)
ax2.set_ylabel('Mortes - Média Móvel de 7 dias',size=15)
ax[1]=df.plot(y='taxa-hosp',style='o-',color='black',ax=ax[1])
ax[1].set_ylabel('Taxa de internação na UTI',size=15)
ax[1].grid()
fig.title('CASOS, ÓBITOS E TAXA DE INTERNAÇÃO EM UTI NA CIDADE DE SÃO PAULO',
          SIZE=20)