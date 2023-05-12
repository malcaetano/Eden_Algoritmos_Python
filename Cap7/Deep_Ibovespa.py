import pandas as pd
import numpy as np
import matplotlib.pyplot as fig
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import datetime as dt
from yahoo_fin.stock_info import *


################ importar a acao ############################
inicio=dt.datetime(2021,1,2)
fim=dt.datetime(2021,11,11)

df_acao = get_data('PETR4.SA', start_date=inicio, end_date=fim)
df_acao.rename(columns={"close":"PETR4.SA"},inplace=True)

df_oleo = get_data('CL=F', start_date=inicio, end_date=fim)
df_oleo.rename(columns={"close":"petroleo"},inplace=True)

df = pd.concat([df_acao, df_oleo[['petroleo','ticker']]], axis=1)
df.dropna(inplace=True)

df['mv5']=df['PETR4.SA'].rolling(window=5).mean()

df.dropna(inplace=True)

df['Preço_aumenta']=np.where(df['PETR4.SA'].shift(-1)>df['PETR4.SA'],1,0)
X=df[['Preço_aumenta','mv5','petroleo']].values
Y=df['PETR4.SA'].values

# Normalização
norma=MinMaxScaler()
norma.fit(X)

X_norm=norma.transform(X)

######### Treinamento e Teste ###################
while True:
        X_norm_train, X_norm_test, Y_train, Y_test= train_test_split(X_norm,
                                                                Y,
                                                               test_size=0.8)
        neuro=MLPRegressor(hidden_layer_sizes=(1000,1000,1000,1000,1000),
                   max_iter=5000,
                   tol=0.0001,
                   learning_rate_init=0.001,
                   solver='sgd',
                   activation='relu',
                   learning_rate='constant',
                   verbose=0)  # verbose=0 (nao mostra passos) 
                               # verbose=2 (mostra passos)
        neuro.fit(X_norm_train, Y_train)
        ######### Previsao no conjunto teste ###################
        Y_prev=neuro.predict(X_norm_test)
        ######## coef. determinacao R2 #######################
        r2=r2_score(Y_test,Y_prev) # coef. determinacao R2 (melhor=1.0)
                                          # R2= Sum(y_est-med)^2/Sum(y-med)^2
        print('score =  ', r2)
        if r2>0.8:
            break

X_test=norma.inverse_transform(X_norm_test)

fig.figure()
fig.scatter(X_test[:,1], Y_test, label='Reais (preço real)')
fig.scatter(X_test[:,1],Y_prev,label='Rede Neural(preço previsto)')
fig.legend(loc=1)
fig.xlabel('Preço da média média móvel')
fig.ylabel('Preço previsto')
##### previsao para dado nao existente no banco de dados ###########
############## lista 1: altas=0 baixas=1 
############## lista 2: preços da media movel
############## lista 3: preços do petroleo em US$
############## Exemplo:
##############  baixa     alta       preco mv   preco mv   preco petr1 preco petr2
##############  entrad1   entrad2    entrad1  entrad2
#Xfut=np.array(  [ [0,     1],        [26,       25]        [84.15   81.7]])
####################################################################

Xfut=np.array(  [ [0,     1,  0],        
                 [26.29,       26.20,   26.29],
                 [84.15, 81.33, 81.58]])
Xfut_norm=norma.transform(Xfut.T)

Y_prev_fut=neuro.predict(Xfut_norm)

print('###############################################')
print('Preço da ação (R$) - Previsão')      
print('Previsão Rede Neural: ', Y_prev_fut)
print('###############################################')
fig.figure()
fig.scatter(X[:,1],Y,label='Real')
fig.scatter(Xfut[1,:],Y_prev_fut, label='Rede Neural')
fig.legend(loc=1)

#fig.figure()
#df['Close']['PETR4.SA'].plot()
#df['mv3'].plot()