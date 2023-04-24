# Teste Cupcake classificador Random Forest
##############################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as fig
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

df = pd.read_excel('Cupcake.xlsx',sheet_name='Planilha1')

print(df.head())
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# formatar para pre-processamento
# se for Muffin label=0
# se nao for Muffin(eh Cupcake) label=1

y=np.where(df['Tipo']=='Muffin',0,1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# transforma as caracteristicas ou titulos de cada coluna em lista
features=df.columns.values[1:].tolist()

X=df[['Flour','Sugar']].values
print(X)

#Create an object (model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
modelo = RandomForestClassifier(n_jobs=-1,random_state=0)

#Fit (train) the model
modelo.fit(X_train, y_train)
previsao=modelo.predict(X_test)
print(previsao)

teste=modelo.predict([[34,23]])
resultado=np.where(teste==0,'Muffin','Cupcake')
print(resultado)
print("Acurácia: ", classification_report(y_test,previsao))




