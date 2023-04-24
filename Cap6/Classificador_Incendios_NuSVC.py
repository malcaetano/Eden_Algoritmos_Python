#########  Machine Learning - NuSVC      ##############
# Classificador de focos de incendios com dados de
# temperatura e umidade como variaveis de entrada
#####################################################
import numpy as np
import pandas as pd
from sklearn.svm import NuSVC
import matplotlib.pyplot as fig
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

sns.set(font_scale=1.2)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#importa dados do Excel
focos=pd.read_excel('Incendios.xlsx',sheet_name='Queimadas')
print(focos.head())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# formatar para pre-processamento
# se for Sim label(com focos)=1
# se nao for Nao(sem focos) label=0

type_label=np.where(focos['Focos']=='Não',0,1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# transforma as caracteristicas ou titulos de cada coluna em lista
focos_features=focos.columns.values[1:].tolist()

var_entrada=focos[['Temp','Umid']].values

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ajuste parametros do modelo
# NuSVC= Support Vector Classification
X_train, X_test, y_train, y_test = train_test_split(var_entrada,
                                                    type_label, 
                                                    test_size=0.3,
                                                    random_state=1) 
modelo=NuSVC(nu=0.1)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(classification_report(y_test,y_pred))

#######################################################
# Plot do treinamento e classificacao de twittie pos e neg
fig.figure()
xx, yy = np.meshgrid(np.linspace(30, 40, 500),
                     np.linspace(30, 70, 500))
################## plot da funcao de decisao do modelo ###

Z = modelo.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

fig.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=fig.cm.Greys)
contours = fig.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linestyles='dashed')
fig.scatter(var_entrada[:, 0], var_entrada[:, 1], s=30, c=type_label,cmap=fig.cm.Paired,
            edgecolors='k')
fig.axis([30, 40, 30, 70])
fig.xlabel('Temperatura(C)')
fig.ylabel('Umidade(%)')

################  teste da previsao com pontos reais ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#cria uma funcao para previsao de "queimadas"(sim) e "não queimadas (não)

def Incendio(Temp,Umid):
      if (modelo.predict([[Temp,Umid]]))==0:
          print('Sem focos de queimadas')
      else:
          print('Com focos de queimadas')
Temp=32    # entrada
Umid=65
Incendio(Temp,Umid) 
fig.plot(Temp,Umid,'ko', markersize='12') 