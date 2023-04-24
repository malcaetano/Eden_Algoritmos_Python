# SENSOR MOMENTO - PANDAS DATAFRAME
# Prof. Dr. Marco Antonio leonel Caetano
# Instituicao: Insper
#################################################################
import matplotlib.pyplot as fig
import datetime as dt
from yahoo_fin.stock_info import *

################ importar a acao ############################
inicio=dt.datetime(2022,1,1)
fim=dt.datetime(2022,8,28)

df = get_data('PETR4.SA', start_date=inicio, end_date=fim)

#++++++++++++++ apagar as colunas volume e adj close +++++++
df=df.drop(['high','low','open','volume','adjclose','ticker'],axis=1)
x=df['close'].values           # <--- transforma coluna em vetor
dif=x[8:]-x[0:-8]              # <---- faz a diferenca por janela na mesma col
df=df.drop(df.index[0:8])      # <---- apaga as 1as 9 linhas iniciais
df['momento']=dif.tolist()     # <---- coloca o vetor em coluna no dataframe

##################### CALCULO DO MOMENTO EM % ###############################
df['momento%']=100*(df['momento'].rolling(window=3).mean())/df['close']

############### calculo do retorno em %  ########################
df['ret']=100*df['close'].pct_change()

################# grafico do fechamento, momento, retorno e histograma #######
df.plot(y=['close','momento%','ret'],subplots=True,
           title=['Fechamentos','Momento%','Retornos(%)'],
           color='black',
           grid=True,
           layout=(2,2))

fig.figure()
df['ret'].plot(kind='hist',density=True,title='Histograma dos retornos',
  color='gray')


######################### estatisticas #########################
print('############## ESTATISTICAS DA AÇÂO ################################')
print('ÚLTIMO PREÇO FECH (R$): %6.3f' % df['close'][-1])      
print('MÁXIMO PREÇO DO FECH(R$): %6.3f' % df['close'].max())     
print('MÍNIMO PREÇO DO FECH(R$): %6.3f'% df['close'].min()) 
print('PREÇO MÉDIO DO FECH(R$): %6.3f' % df['close'].mean()) 
print('MÁXIMO RETORNO DO FECH(porcent): ', round(df['ret'].max(),3) )
print('DIA DO MÁXIMO RETORNO FECH: ', df.index[df['ret'].argmax()]) 
print('MÍNIMO RETORNO DO FECH(porcent): ' , round(df['ret'].min(),3) )
print('DIA DO MÍNIMO RETORNO FECH: ', df.index[df['ret'].argmin()])
print('VOLATILIDADE (desv.pad. pop) DOS PREÇOS DE FECH: %6.3f' % df['close'].std(ddof=0)) 
print('VOLATILIDADE (desv.pad. pop) DOS RETORNOS DE FECH (porcent): ', round(df['ret'].std(ddof=0),3) )
print('####################################################################')

      




    