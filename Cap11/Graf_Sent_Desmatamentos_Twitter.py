import pandas as pd
import matplotlib.pyplot as fig

##############################################################
# Buscando dados do Excel
#############################################################
fatos=pd.read_excel('Res_Eventos.xlsx',sheet_name='Planilha1')
nomes=['data','desmatamento','queimadas','Amazonia','agricultura','indústria']
##############################################################
# reajustando o indice do DataFrame para data
df=pd.DataFrame(fatos[-26536:-13057],columns=nomes)
df=df.reset_index()

df.plot.line(y=[nomes[1],nomes[2],nomes[3]],
             subplots=True,
             layout=(3,1),
             color='k',
             label=['desmatamentos','incêndios','amazonia'])
fig.text(0,-1,'26-Março-2021',fontsize=14,color='k',weight='bold')
fig.text(x=12100,y=-1,s='03-Outubro-2021',fontsize=14,color='k',weight='bold')

