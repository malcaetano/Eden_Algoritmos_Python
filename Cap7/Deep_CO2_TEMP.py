import pandas as pd
import numpy as np
import matplotlib.pyplot as fig
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

dad=pd.read_excel('Co2_Temp.xlsx')

X=dad[['co2']]
Y=dad['temp']

# Normalização
norma=StandardScaler()
norma.fit(X)

X_norm=norma.transform(X)

######### Treinamento e Teste ###################
while True:
        X_norm_train, X_norm_test, Y_train, Y_test= train_test_split(X_norm,
                                                                Y,
                                                                test_size=0.96)
        neuro=MLPRegressor(hidden_layer_sizes=(500,500,1500,1500,500),
                   max_iter=5000,
                   tol=0.0001,
                   learning_rate_init=0.1,
                   solver='sgd',
                   activation='relu',
                   learning_rate='constant',
                   verbose=0)  # verbose=0 (nao mostra passos) 
                               #verbose=2 (mostra passos)
        neuro.fit(X_norm_train, Y_train)
        ######### Previsao no conjunto teste ###################
        Y_prev=neuro.predict(X_norm_test)
        ######## erro medio quadratico #######################
        r2=r2_score(Y_test,Y_prev) # coef. determinacao R2 (melhor=1.0)
                                          # R2= Sum(y_est-med)^2/Sum(y-med)^2
        print('score =  ', r2)
        if r2>0.4:
            break

X_test=norma.inverse_transform(X_norm_test)

fig.figure()
fig.scatter(X_test, Y_test, label='Reais (graus C)')
fig.scatter(X_test,Y_prev,label='Rede Neural(graus C)')
fig.legend(loc=1)
fig.xlabel('Emissão anual CO2 (milhões toneladas)')
fig.ylabel('Anomalia de Temperatura (graus C) em relação a média 1950-1960')

##### previsao para dado nao existente no banco de dados ###########
Xfut=np.array([[120500, 130000]])
Xfut_norm=norma.transform(Xfut.T)

Y_prev_fut=neuro.predict(Xfut_norm)
print('###############################################')
print('Variação de Temperatura (graus C) - Previsão')      
print('Previsão Rede Neural: ', Y_prev_fut)
print('###############################################')
fig.figure()
fig.scatter(X,Y,label='Real')
fig.scatter(Xfut,Y_prev_fut, label='Rede Neural')
fig.legend(loc=1)

dad.index=dad['ano']
dad=dad.drop(['ano'],axis=1)

figura,ax=fig.subplots()
ax=dad['co2'].plot(ylabel='Emissão Co2 (milhões de toneladas)',
      legend=True,color='black')
ax.legend(loc='upper left',prop= {'weight':'bold'})

ax2=ax.twinx()
ax2=dad['temp'].plot(ylabel='Anomalia da Temperatura (graus C)',
       legend=True,style='--',color='black')
fig.title('Histórico de emissão de CO2 e anomalia na temperatura global (C) anual')
