#Queimadas - comparacao com twitter
# mensagens com sentimentos positivos e negativos em relacao a
# palavra-chave: queimadas
###########################################################
import pandas as pd
import matplotlib.pyplot as fig

df=pd.read_excel('Queimadas_dia.xlsx',
                  sheet_name='Planilha1')

df['mvFoc']=df['Focos'].rolling(window=7).mean()
df['mvPos']=df['Queim_pos'].rolling(window=7).mean()
df['mvNeg']=df['Queim_neg'].rolling(window=7).mean()

ax=df.plot(x='data',y='Focos',xlabel='DATA',
           legend=True,color='black',linewidth=3,alpha=0.5)
ax.legend(['Focos de Incêndios'],loc='upper left',prop= {'weight':'bold'})
fig.title('Comparação entre dados de focos de incêndio na AM e média móvel os sentimentos nas mensagens do Twitter sobre a Amazônia',
          size=15)
ax.set_ylabel('FOCOS DE INCÊNDIOS',size=16)

ax2=ax.twinx()
ax=df.plot(x='data',y='mvPos',color='black',
           legend=True,linewidth=1,ax=ax2,
           style='-o',ms=4)

ax=df.plot(x='data',y='mvNeg',color='black',
           legend=True,linewidth=1,ax=ax2,
           style='--')
ax2.set_ylabel('ANÁLISE DE SENTIMENTO NO TWITTER',size=16)
ax2.legend(['Comentários Positivos','Comentários Negativos'],
           loc='upper right',prop= {'weight':'bold'})

