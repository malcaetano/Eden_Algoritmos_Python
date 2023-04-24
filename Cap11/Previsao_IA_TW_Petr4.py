# previsao numerica - Machine Learning com  Decision Tree
##############################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as fig
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_excel('Sentimento_PETR4.xlsx',sheet_name='Planilha1')
df=df.drop('Data',1)
print(df.head())
# Entrada para os dados de Machine Learning
X = df[['TWPetr4','Pib','Inflação','Desemprego','Indústria']] 
# Saida para previsao
y = df['Fech']   

#Cria o modelo de previsao
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)

modelo = DecisionTreeRegressor(max_depth=15,min_samples_split=3)

#Fit (treinamento) do Modelo
modelo.fit(X_train, y_train)

#Previsao dos precos da PETR4 com o modelo gerado
previsao=modelo.predict(X_test)

################### calculo do erro medio quadratico do modelo ######
mean_squared_error=np.mean((y_test.values-modelo.predict(X_test))**2)
rmse=np.sqrt(mean_squared_error)
print('++++++++++++++++++++++++++++++')
print('Erro médio quadrático ', rmse)

########################### Previsao do Machine Learning ##########
print('############ previsão  ###########')

r=pd.DataFrame(df.iloc[:,1:6])   
prev=pd.DataFrame(r.values)
Yprev=modelo.predict(prev)
print(' prev dia fut = ' , Yprev)
print(' ')
saida=pd.DataFrame(Yprev)
saida['med_mov']=saida.rolling(window=2).mean()

print('++++++++++++++++++++++++++++++++++++++++++++')
print(' Previsão Preço PETR4')
print('++++++++++++++++++++++++++++++++++++++++++++')
Yprev_mean = np.mean(y_test)
Yprev_std = np.std(y_test)
teste=modelo.predict([[0.167,0.028,-0.017,0.0233,-0.01]])
print(teste-2*Yprev_std/np.sqrt(len(df)),teste+2*Yprev_std/np.sqrt(len(df)))
print('++++++++++++++++++++++++++++++++++++++++++++')

######################### Graficos da Previsao dos Precos ##################
dias=np.arange(0,len(df))

fig.figure()
sns.lineplot(x=dias,y=df['Fech'],color='black')
sns.lineplot(x=dias, y=saida['med_mov'], linestyle='--', color='black')
fig.fill_between(dias, saida['med_mov'] + 2*Yprev_std/np.sqrt(len(df)), 
                 saida['med_mov'] - 2*Yprev_std/np.sqrt(len(df)), 
                 alpha=0.5, color='gray')
fig.legend(['Real','Previsto'])
fig.xlabel('dias', fontsize=14)
fig.ylabel('Preços da Ação (estimativa, real)', fontsize=14)
fig.title('PREVISÃO DOS PREÇOS DA AÇÃO PETR4 COM MACHINE LEARNING E TWITTER',
          fontsize=14,weight='bold')

############ Previsao apos o horario de fechamento da Bovespa #############
ForaH = pd.read_excel('Sentimento_PETR4.xlsx',sheet_name='Fora_horario')
teste=modelo.predict(ForaH)
teste_mean = np.mean(teste)
teste_std = np.std(teste)
print('++++++++++++++++++++++++++++++++++++++++++++')
print(' Previsão Preço PETR4 - FORA DO HORÁRIO DO MERCADO')
print('++++++++++++++++++++++++++++++++++++++++++++')

print(teste_mean-2*teste_std/np.sqrt(len(teste)),
      teste_mean+2*teste_std/np.sqrt(len(teste)))
fig.figure()
fig.plot(teste,'-ok')
fig.title('PREVISÃO DOS PREÇOS DA AÇÃO APOÓS HORÁRIO DE FECHAMENTO DA BOVESPA')
fig.ylabel('preços em reais R$', fontsize=14)






