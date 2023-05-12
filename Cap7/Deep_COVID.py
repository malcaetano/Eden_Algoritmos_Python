# Deep Learning Covid-19 Cidade de Sao Paulo
import pandas as pd
import numpy as np
import matplotlib.pyplot as fig
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

df=pd.read_excel('Covid_SP.xlsx')
df['taxa-hosp']=df['UTImd7dias'].diff()
df.index=df['data']
df=df.drop(['data','UTImd7dias'],axis=1)
df['Caso7d']=df['Casos'].rolling(window=7).mean()
df['Morte7d']=df['Mortes'].rolling(window=7).mean()
df.dropna(inplace=True)
print(df)

df['Caso_aumenta']=np.where(df['Caso7d'].shift(-1)>df['Caso7d'],1,0)
X=df[['Caso_aumenta','Caso7d','taxa-hosp']].values
Y=df['Morte7d'].values

# Normalização
norma=MinMaxScaler()
norma.fit(X)

X_norm=norma.transform(X)

######### Treinamento e Teste ###################
while True:
        X_norm_train, X_norm_test, Y_train, Y_test= train_test_split(X_norm,
                                                                Y,
                                                               test_size=0.7)
        neuro=MLPRegressor(hidden_layer_sizes=(50,50),
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
        ######## erro medio quadratico #######################
        r2=r2_score(Y_test,Y_prev) # coef. determinacao R2 (melhor=1.0)
                                          # R2= Sum(y_est-med)^2/Sum(y-med)^2
        print('score =  ', r2)
        if r2>0.9:
            break

X_test=norma.inverse_transform(X_norm_test)

fig.figure()
fig.scatter(X_test[:,1], Y_test, label='Mortes (real)')
fig.scatter(X_test[:,1],Y_prev,label='Mortes(previsto)')
fig.legend(loc=1)
fig.xlabel('Casos média 7 dias')
fig.ylabel('Mortes (previsão)')
##### previsao para dado nao existente no banco de dados ###########
############## lista 1: altas=0 baixas=1 
############## lista 2: casos da media movel
############## lista 3: taxa de hospitalizacao UTI media 7 dias
############## Exemplo:
##############  baixa     alta       casos   casos       UTI     UTI
##############  entrad1   entrad2    entrad1  entrad2
#Xfut=np.array(  [ [0,     1],        [26,       27]    [10     11]])
####################################################################

Xfut=np.array(  [ [1,     1,  0],        
                 [111,       52,   88],
                 [-26, -15, -13]])
Xfut_norm=norma.transform(Xfut.T)

Y_prev_fut=neuro.predict(Xfut_norm)

print('###############################################')
print('Preço da ação (R$) - Previsão')      
print('Previsão Rede Neural: ', Y_prev_fut)
print('###############################################')
fig.figure()
fig.scatter(X[:,2],Y,label='Real')
fig.scatter(Xfut[2,:],Y_prev_fut, label='Rede Neural')
fig.legend(loc=1)

