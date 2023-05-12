# Deep Learning Covid-19 Cidade de Sao Paulo
import pandas as pd
import matplotlib.pyplot as fig
import numpy as np

df=pd.read_excel('Covid_SJC.xlsx')
df['taxa-hosp']=df['UTImd7dias'].diff()
df.index=df['data']
df=df.drop(['data','UTImd7dias'],axis=1)
df['Caso7d']=df['Casos'].rolling(window=7).mean()
df['Morte7d']=df['Mortes'].rolling(window=7).mean()
df.dropna(inplace=True)
print(df)

figura,ax=fig.subplots()
ax=df['Caso7d'].plot()
ax.set_yticks(np.arange(0, df['Caso7d'].max(), 200))
ax.set_ylabel('Casos',size=16)
ax.legend(loc='upper left',prop= {'weight':'bold'})
fig.title('Covid-19 Cidade de São José dos Campos',size=18)

ax2=ax.twinx()
ax2=df['taxa-hosp'].plot(ylabel='Taxa de Internados na UTI - média 7 dias',
      legend=True,color='red',alpha=0.6)
ax2.set_ylabel('Taxa de Internados na UTI - média 7 dias',size=16)

ax3=ax.twinx()
ax3.spines['left'].set_position(('axes', 0.05))

ax3=df['Morte7d'].plot(color='black',legend=True)
ax3.yaxis.tick_left()
ax3.yaxis.set_label_position("left")
ax3.set_ylabel('Mortes',size=16)
ax3.legend(loc='center left', bbox_to_anchor=(0.5, 0.98),prop= {'weight':'bold'})
ax3.set_yticks(np.arange(0, df['Morte7d'].max(), 1))
ax3.grid()