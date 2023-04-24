import pandas as pd
import matplotlib.pyplot as fig

##############################################################
# Buscando dados do Excel
#############################################################
fatos=pd.read_excel('Sentimento_PETR4.xlsx',sheet_name='Planilha1')
nomes=['Data','Fech','TWPetr4','Pib','Inflação','Desemprego','Indústria']
##############################################################
# reajustando o indice do DataFrame para data
df=pd.DataFrame(fatos,columns=nomes)
df=df.reset_index()

df.plot.line(y=[nomes[2],nomes[3],nomes[4]],
             subplots=True,
             layout=(3,1),
             color='k',
             label=['PETR4','Pib','Inflação'])
fig.text(1,-0.5,'16-Setembro-2021',fontsize=14,color='k',weight='bold')
fig.text(x=220,y=-0.5,s='30-Setembro-2021',fontsize=14,color='k',weight='bold')

df.plot.line(y=nomes[1], color='k', label='PETR4')
fig.text(1,23.2,'16-Setembro-2021',fontsize=14,color='k',weight='bold')
fig.text(x=220,y=23.2,s='30-Setembro-2021',fontsize=14,color='k',weight='bold')
fig.ylabel('Preços da ação PETR4', fontsize=14, weight='bold', color='k')
fig.grid()
