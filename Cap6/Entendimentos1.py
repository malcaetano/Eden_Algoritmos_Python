#+++++++++++++++++++++++++++++++++++++++ 
# Decision Tree Regressor
# reta Y = 3*X1
#+++++++++++++++++++++++++++++++++++++++
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as fig
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_excel('Reta.xlsx',sheet_name='Planilha1')

X = df[['X1']] # variavel independente (pd DataFrame)
y = df['Y']   # variavel dependente (pd Series)

############## Cria o modelo de regressao #############################
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=2,
                                                    shuffle=True)
modelo = DecisionTreeRegressor(max_depth=4,min_samples_split=2)

############  treino do modelo ####################################
modelo.fit(X_train, y_train)
mean_squared_error=np.mean((y_test.values-modelo.predict(X_test))**2)
rmse=np.sqrt(mean_squared_error)
print('Erro médio quadrático ', rmse)

print('############ previsão  ###########')
r=pd.DataFrame(df.iloc[:,1:2])   
prev=pd.DataFrame(r.values)
Yprev=modelo.predict(prev)
print(' prev dia fut = ' , Yprev)

################## grafico da previsao e do resultado correto ##########
sns.lineplot(x=df['X1'],y=df['Y'],color='black')
sns.lineplot(x=df['X1'], y=Yprev,style=True,dashes=[(4,1)], color='black')
fig.legend(['Real','Previsto'])
fig.xlabel('dias')
fig.ylabel('Função')


