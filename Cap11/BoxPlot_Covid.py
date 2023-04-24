import matplotlib.pyplot as fig
import pandas as pd

dados=pd.read_excel('COVID_BOX.xlsx',sheet_name='Casos')
df=pd.DataFrame(dados)
df=df.set_index('data')

df1=df.iloc[:,0:28].rolling(window=14,min_periods=0).mean()

fig.figure()
ax1=fig.subplot(111)
klist=['SP']
for i in klist:
     ax1.plot(df.index,df[i],color='grey')
     ax1.plot(df1.index,df1[i],color='black',lw=5)
     ax1.set_xlabel('Fev-Set 2020',fontsize=16)
     ax1.set_ylabel('Casos de Covid-19',fontsize=16)

fig.title('Covid-19 ---- (MÉDIA MÓVEL DE 14 DIAS / CASOS DIÁRIOS) NO ESTADO DE SP',
          fontsize=18)




