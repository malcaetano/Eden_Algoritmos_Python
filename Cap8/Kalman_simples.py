### Filtro de Kalman para movimento unif. variado
import numpy as np
import matplotlib.pyplot as fig
import seaborn as sns
from scipy.stats import norm

####### inicializacao das listas para armazenar os dados
estado_S=[]
estado_V=[]
ruido_estado=[]
ruido_medida=[]
medida=[]
tempo=[]
##############################################################
X=np.array([[0], [0]])      # <--- posicao e velocidade iniciais "reais"
dt=0.1                      # <--- incremento no tempo

################### Matrizes do Modelo ######################
A=np.array([[1, dt],[0, 1]])   # <------- Modelo posicao e veloc

B=np.array([[dt**2/2],[dt]])   # <------- Matriz da aceleracao

C=np.array([1,0])      # indica que o sensor é apenas de posicao

a=0.1                        # <--- valor da acelaracao cte

################### Ruidos #################################
desv_s=0.01             # < ---- ruido da posicao
desv_v=0.02             # < ---- ruido na velocidade
desv_y=5                # ruido na medida da posicao

################## Matrizes de Covariancia #############
                # Covariancia do ruido do estado
Q=np.array([[desv_s**2,0],[0,desv_v**2]])

                # Covariancia do ruido de medida
R=desv_y**2
#######################################################
# Simulacao do Movimento +++++++++++++++++++++++++++

t = 0
tfinal=30

while t<=tfinal:
    ws = np.random.randn(1)   # var aleatoria normal(0,1)
    wv = np.random.randn(1)   # var aleatoria normal(0,1)
# ---------------- geracao do ruido de posicao e velocidade ----    
    W=np.matmul(np.sqrt(Q),np.array([ws,wv])) 
#----------------- modelo de estado com ruido -------------------    
    X = np.matmul(A,X) + B*a + W 
#---------------- modelo da medida com ruido ------------------    
    eta=np.sqrt(R) * np.random.randn(1)
    Y = np.matmul(C,X) + eta 
#----------------- salvando os valores em lista para figuras ----    
    estado_S.append(X[0])     # salva a posicao
    estado_V.append(X[1])     # salva a velocidade
    ruido_estado.append(W[0]) # salva o ruido de posicao
    ruido_medida.append(eta)  # salva o ruido de medida da posicao
    medida.append(Y)          # salva a medida Y da posicao 
    tempo.append(t)           # salva o tempo decorrido
    t = t + dt

########## transforma a lista do ruido em vetor para o histograma ####
ruido_estado=np.array(ruido_estado)

###################### Figuras ##################################
fig.figure()
fig.plot(tempo,estado_S,color='Black',linewidth=4)
fig.plot(tempo,medida,color='Black',alpha=0.5)
fig.grid()
fig.xlabel('tempo')
fig.ylabel('posição S(k)')
fig.title('Localização com modelo de estado S(k) e medida com ruído')

fig.figure()
sns.distplot(ruido_medida, kde=False, fit=norm,
             hist_kws={"histtype": "step", "linewidth": 3,
                            "alpha": 0.5, "color": "k"})
fig.title('Ruído de medida n(k) da posição')    


