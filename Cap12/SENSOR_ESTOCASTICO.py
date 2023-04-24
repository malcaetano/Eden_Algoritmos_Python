# SENSOR ESTOCASTICO - PANDAS DATAFRAME
# Prof. Dr. Marco Antonio leonel Caetano
# Instituicao: Insper
#################################################################
import matplotlib.pyplot as fig
import datetime as dt
import seaborn as sns
from yahoo_fin.stock_info import *
################ importar a acao ############################
inicio=dt.datetime(2022,1,1)
fim=dt.datetime(2022,8,28)

df = get_data('PETR4.SA', start_date=inicio, end_date=fim)

#++++++++++++++ apagar as colunas volume e adj close +++++++
df=df.drop(['volume','adjclose'],axis=1)
############################################################

############### calculo do retorno ########################
df['ret']=df['close'].pct_change()
###########################################################

################# grafico do fechamento e retorno ############
df.plot(y=['close','ret'],subplots=True,
        title=['Fechamentos','Retornos'],color=['black','black'])

################# calculo do estocastico ##################
# cria as colunas necessarias para os calculos do sensor
# min30: minimo de 30 em 30 dias
# max30: maximo de 30 em 30 dias
# estocast: 100*(fech-min30)/(max30-min30)

df['min30']=df['close'].rolling(window=30,min_periods=30).min()
df['max30']=df['close'].rolling(window=30,min_periods=30).max()
df['estocast']=100*((df['close']-df['min30'])/(df['max30']-df['min30']))
df['med_mov']=df['close'].rolling(window=30).mean()

########### imprime o dataframe completo
print(df)

########## grafico em subplot fech e sensor
df.plot(y=['close','estocast'],subplots=True,
        title=['Fechamentos','Estocástico'],
        color=['black','black'])

######## grafico comparando media movel e fechamento ######
df.plot(y=['close','med_mov'],
        title='Comparação entre Fechamento e Média Móvel 30 dias',
        color=['black','black'])

######### grafico em subplot do retorno a esquera e histograma do
######### retorno a direita
df.dropna(inplace=True)
fig.figure()
fig.subplot(121)
fig.plot(df.index,df['ret'].values,color='black')
fig.xticks(rotation=30)
fig.title('Retornos')
fig.subplot(122)
sns.distplot(df['ret'],color='black')
fig.title('Histograma dos Retornos')

############# apaga as colunas do calculo do estocastico para salvar
#####         em outro dataframe para fazer o boxplot diario
##### isso eh necessario pois precisamos fazer a transposta da 
##### matriz para ver o boxplot dia a dia

dfbox=df.drop(['min30','max30','estocast','med_mov','ret','ticker'],axis=1)

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
