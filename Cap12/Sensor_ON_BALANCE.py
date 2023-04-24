# SENSOR On Balance Volume (OBV) - PANDAS DATAFRAME
# Prof. Dr. Marco Antonio leonel Caetano
# Instituicao: Insper
#################################################################
import matplotlib.pyplot as fig
import datetime as dt
import seaborn as sns
import numpy as np
from yahoo_fin.stock_info import *

################ importar a acao ############################
inicio=dt.datetime(2022,1,1)
fim=dt.datetime(2022,8,28)
df = get_data('PETR4.SA', start_date=inicio, end_date=fim)

#++++++++++++++ apagar as colunas volume e adj close +++++++
df=df.drop(['adjclose'],axis=1)
############################################################

############### calculo do retorno ########################
df['ret']=df['close'].pct_change()
###########################################################

################# grafico do fechamento e retorno ############
df.plot(y=['close','ret'],subplots=True,title=['Fechamentos','Retornos'],
        color='black',style=['-o','-'],grid=True)

################# calculo do OBV     ##################
# cria as colunas necessarias para os calculos do sensor
df['OBV']=0

for i in range(len(df)):
    if i==0:
        df['OBV'][i]=df['volume'][i]
    else:    
         if df['close'][i]>df['close'][i-1]:
                df['OBV'][i]=df['OBV'][i-1]+df['volume'][i]
         elif df['close'][i]<df['close'][i-1]:       
                df['OBV'][i]=df['OBV'][i-1]-df['volume'][i]
         else:
                df['OBV'][i]=df['OBV'][i-1]

df['med_mov']=df['close'].rolling(window=3).mean()

x1=df['close'].values
x2=df['OBV'].values
lin=len(x1)
eix=np.linspace(1,lin,lin)
coef1=np.polyfit(eix,x1,1)
tendencia_fech= coef1[0]*eix + coef1[1]

coef2=np.polyfit(eix,x2,1)
tendencia_OBV= coef2[0]*eix + coef2[1]
df['tend_fech']=tendencia_fech.tolist()
df['tend_OBV']=tendencia_OBV.tolist()
########### imprime o dataframe completo
print(df)

########## grafico em subplot fech e sensor
figure=fig.figure()
ax1=figure.add_subplot(211)
ax2=figure.add_subplot(212)
df.plot(y=['close','tend_fech'],title='Fechamentos',
         ax=ax1, style=['-','--'], color=['black','black'])
df.plot(y=['OBV','tend_OBV'],title='On Balance Volume',
         ax=ax2, style=['-','--'],color=['black','black'])
######## grafico comparando media movel e fechamento ######
df.plot(y=['close','med_mov'],
        color='black',
        style=['-','--'],
        title='Comparação entre Fechamento e Média Móvel 7 dias')

######### grafico em subplot do retorno a esquera e histograma do
######### retorno a direita
#df.dropna(inplace=True)
fig.figure()
fig.subplot(121)
fig.plot(df.index,df['ret'].values,color='black')
fig.xticks(rotation=30)
fig.title('Retornos')
fig.subplot(122)
sns.distplot(df['ret'],color='gray')
fig.title('Histograma dos Retornos')

############# apaga as colunas do calculo do OBV para salvar
#####         em outro dataframe para fazer o boxplot diario
##### isso eh necessario pois precisamos fazer a transposta da 
##### matriz para ver o boxplot dia a dia

dfbox=df.drop(['OBV','med_mov','ret','volume','tend_fech','tend_OBV','ticker'],axis=1)

############## figura plotando juntos as curvas de fechamento e boxplot #######
figura,ax=fig.subplots()
ax.plot(df['close'].values[-30:],color='black')
dfbox[-30:].T.boxplot(color='black')

fig.xticks(rotation=30) #---> rotaciona as datas em 30 graus no eixo x
fig.title('Boxplot dos Fechamentos')

######################### estatisticas #########################
print('############## ESTATISTICAS DA AÇÂO ################################')
print('ÚLTIMO PREÇO FECH (R$): %6.3f' % df['close'][-1])      
print('MÁXIMO PREÇO DO FECH(R$): %6.3f' % df['close'].max())     
print('MÍNIMO PREÇO DO FECH(R$): %6.3f'% df['close'].min()) 
print('PREÇO MÉDIO DO FECH(R$): %6.3f' % df['close'].mean()) 
print('MÁXIMO RETORNO DO FECH(porcent): ', 100 * round(df['ret'].max(),3) )
print('DIA DO MÁXIMO RETORNO FECH: ', df.index[df['ret'].argmax()]) 
print('MÍNIMO RETORNO DO FECH(porcent): ' , 100 * round(df['ret'].min(),3) )
print('DIA DO MÍNIMO RETORNO FECH: ', df.index[df['ret'].argmin()])
print('VOLATILIDADE (desv.pad. pop) DOS PREÇOS DE FECH: %6.3f' % df['close'].std(ddof=0)) 
print('VOLATILIDADE (desv.pad. pop) DOS RETORNOS DE FECH (porcent): ', 100* round(df['ret'].std(ddof=0),3) )
print('####################################################################')
