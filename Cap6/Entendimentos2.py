# Teste Regressor
# reta Y = Cos(X1)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as fig
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_excel('Cosseno.xlsx',sheet_name='Planilha1')
print(df.head())

X = df[['X1']] #Two-dimensional (pd DataFrame)
y = df['Y']   #One-dimensional (pd Series)

#Create an object (model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=2,
                                                    shuffle=True)
modelo = DecisionTreeRegressor(max_depth=4,min_samples_split=2)

#Fit (train) the model
modelo.fit(X_train, y_train)

mean_squared_error=np.mean((y_test.values-modelo.predict(X_test))**2)
rmse=np.sqrt(mean_squared_error)
print('Erro médio quadrático ', rmse)


print('############ previsão  ###########')


r=pd.DataFrame(df.iloc[:,1:2])   
prev=pd.DataFrame(r.values)
Yprev=modelo.predict(prev)
print(' prev dia fut = ' , Yprev)

fig.figure()
sns.lineplot(x=df['X1'],y=df['Y'],color='black')
sns.lineplot(x=df['X1'], y=Yprev,style=True,dashes=[(4,1)], color='black')
fig.legend(['Real','Previsto'])
fig.xlabel('dias')
fig.ylabel('Função')

r2=np.linspace(0,5,10)
prev2=pd.DataFrame(r2)
Yprev2=modelo.predict(prev2)
print(' prev dia fut = ' , Yprev2)

fig.figure()
sns.lineplot(x=r2,y=Yprev2)
