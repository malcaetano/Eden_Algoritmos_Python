#########  Machine Learning - SVM      ##############
# Classificador de focos de incendios com dados de
# temperatura e umidade como variaveis de entrada
#####################################################
import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as fig
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split

sns.set(font_scale=1.2)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#importa dados do Excel
focos=pd.read_excel('Incendios.xlsx',sheet_name='Queimadas')
print(focos.head())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# plot nossos dados
sns.lmplot('Temp','Umid',data=focos,hue='Focos',fit_reg=False,
           palette='gray_r', markers=['o','x'])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# formatar para pre-processamento
# se for Sim label(com focos)=1
# se nao for Nao(sem focos) label=0

type_label=np.where(focos['Focos']=='Não',0,1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# transforma as caracteristicas ou titulos de cada coluna em lista
focos_features=focos.columns.values[1:].tolist()

var_entrada=focos[['Temp','Umid']].values
print(var_entrada)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ajuste parametros do modelo
# SVC= Support Vector Classification
X_train, X_test, y_train, y_test = train_test_split(var_entrada,
                                                    type_label, 
                                                    test_size=0.3,
                                                    random_state=0) 
modelo=svm.SVC(kernel='linear')
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# separacao do hiperplano
w=modelo.coef_[0]
a=-w[0]/w[1]
xx=np.linspace(30,35)
yy=a*xx-(modelo.intercept_[0])/w[1]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# plot a separacao do hiperplano feito pelo SVC
margem=1/np.sqrt(np.sum(modelo.coef_**2))
yy_baixo=yy-np.sqrt(1+a**2)*margem
b=modelo.support_vectors_[-1]
yy_alto=yy+np.sqrt(1+a**2)*margem

sns.lmplot('Temp','Umid',data=focos,hue='Focos',fit_reg=False,
           palette='gray_r', markers=['o','x'])
fig.plot(xx,yy,linewidth=2,color='black')
fig.plot(xx,yy_baixo,'k--')
fig.plot(xx,yy_alto,'k--')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#cria uma funcao para previsao de "queimadas"(sim) e "não queimadas (não)

def Incendio(Temp,Umid):
      if (modelo.predict([[Temp,Umid]]))==0:
          print('Sem focos de queimadas')
      else:
          print('Com focos de queimadas')
Temp_prev=32
Umid_prev=65          
Incendio(Temp_prev,Umid_prev) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# plot o ponto de previsao para comparacao de acerto

sns.lmplot('Temp','Umid',data=focos,hue='Focos',fit_reg=False,
           palette='gray_r', markers=['o','x'])
fig.plot(xx,yy,linewidth=2,color='black')
fig.plot(Temp_prev,Umid_prev,'ko', markersize='12')      
fig.plot(xx,yy,linewidth=2,color='black')
fig.plot(xx,yy_baixo,'k--')
fig.plot(xx,yy_alto,'k--')

############### Calculo da precisao do treinamento ####################
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
  