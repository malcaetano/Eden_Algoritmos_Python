import pandas as pd
import numpy as np
import matplotlib.pyplot as fig
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

dad=pd.read_excel('Teste2Ent.xlsx')

fig.scatter(dad[['x1']],dad[['y']])
fig.scatter(dad[['x2']],dad[['y']])
fig.xlabel('x')
fig.ylabel('y')

X=dad[['x1','x2']]
Y=dad['y']

# Normalização
norma=StandardScaler()
norma.fit(X)

X_norm=norma.transform(X)

######### Treinamento e Teste ###################
X_norm_train, X_norm_test, Y_train, Y_test= train_test_split(X_norm,Y,test_size=0.3)

#### Processamento - aprendizado de maquina
# rede neural de multipla camada
### a tupla (10,5,) indica duas camadas escondidas, com 10 neuronios na 1a
### e 5 neuronios na segunda

neuro=MLPRegressor(hidden_layer_sizes=(20,),
                   max_iter=5000,
                   tol=0.0001,
                   learning_rate_init=0.1,
                   solver='sgd',
                   activation='logistic',
                   learning_rate='constant',
                   verbose=2)
neuro.fit(X_norm_train, Y_train)

######### Previsao no conjunto teste ###################
Y_prev=neuro.predict(X_norm_test)

######## erro medio quadratico #######################
r2=r2_score(Y_test,Y_prev)
print('Erro médio quadrático ', r2)

X_test=norma.inverse_transform(X_norm_test)

fig.figure()
fig.scatter(X_test[:,0], Y_test, label='Reais')
fig.scatter(X_test[:,0],Y_prev,label='Rede Neural')
fig.legend(loc=1)

##### previsao para dado nao existente no banco de dados ###########
Xfut=np.array([[61, 32],[65,33]])

Xfut_norm=norma.transform(Xfut.T)

Y_prev_fut=neuro.predict(Xfut_norm)
print('Previsão Rede Neural: ', Y_prev_fut)

fig.figure()
fig.scatter(X['x1'],Y,label='Real')
fig.scatter(Xfut[:,0],Y_prev_fut, label='Rede Neural')
fig.legend(loc=1)
