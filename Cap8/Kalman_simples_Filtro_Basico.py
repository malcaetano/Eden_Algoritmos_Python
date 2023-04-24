### Filtro de Kalman para movimento unif. variado
import numpy as np
import matplotlib.pyplot as fig
import seaborn as sns
from scipy.stats import norm
from numpy.linalg import inv

####### inicializacao das listas para armazenar os dados
estado_S=[]
estado_V=[]
estado_Se=[]
estado_Ve=[]
medida=[]
covP=[]
tempo=[]
##############################################################
X=np.array([[0], [0]])      # <--- posicao e velocidde iniciais "reais"
Xe=np.array([[0],[0]])      # <--- posicao e velocidade do modelo estimado
dt=0.1                      # <--- incremento no tempo

################### Matrizes do Modelo ######################
A=np.array([[1, dt],[0, 1]])   # <------- Modelo posicao e veloc

B=np.array([[dt**2/2],[dt]])   # <------- Matriz da aceleracao

C=np.array([1,0])      # indica que o sensor é apenas de posicao

a=0.1                        # <--- valor da acelaracao cte

################### Ruidos #################################
desv_s=0.05             # < ---- ruido da posicao
desv_v=0.05             # < ---- ruido na velocidade
desv_y=1                # ruido na medida da posicao

################## Matrizes de Covariancia #############
                # Covariancia do ruido do estado
Q=np.array([[desv_s**2,0],[0,desv_v**2]])

                # Covariancia do ruido de medida
R=desv_y**2
#######################################################
# Equacao da leitura do sensor
Psi=np.sqrt(R) * np.random.randn(1)
Y = np.matmul(C,X) + Psi 
######################################################

P = Q                       # covariancia inicial



# Simulacao do Movimento +++++++++++++++++++++++++++
t = 0
tfinal=30

estado_S.append(X[0])     # salva a posicao
estado_V.append(X[1])     # salva a velocidade
estado_Se.append(Xe[0])     # salva a posicao estimada
estado_Ve.append(Xe[1])     # salva a velocidade estimada
medida.append(Y)          # salva a medida Y da posicao 
covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
tempo.append(t)           # salva o tempo decorrido
    
while t<=tfinal:
    ws = np.random.randn(1)   # var aleatoria normal(0,1)
    wv = np.random.randn(1)   # var aleatoria normal(0,1)
# ---------------- geracao do ruido de posicao e velocidade ----    
    W=np.matmul(np.sqrt(Q),np.array([ws,wv])) 
#----------------- modelo de estado com ruido -------------------    
    X = np.matmul(A,X) + B*a + W 
#---------------- modelo de estado estimado -------------------
    Xe = np.matmul(A,Xe) + B*a 
#----------------- covariancia do estado -----------------
    P = np.matmul(np.matmul(A,P),np.transpose(A)) + np.matmul(np.matmul(C,Q),np.transpose(C))    
#----------------- estimador do sensor de medida ------------
    Z = np.matmul(C,Xe)   
#---------------- modelo da medida com ruido ------------------    
    Psi=np.sqrt(R) * np.random.randn(1)
    Y = np.matmul(C,X) + Psi 
###################################################################
###### Filtro de Kalman #############################################
# +++++ ganho K
    k1= np.matmul(P,np.transpose(C))
    k2= np.matmul(np.matmul(C,P),np.transpose(C)) + R
    K = k1/k2
    Xe = Xe + K[:,np.newaxis]*(Y-Z) 
    p1 = P
    p2 = inv(np.identity(len(Q)) + np.matmul(K,C))
    P = np.matmul(p1,p2)   
#----------------- salvando os valores em lista para figuras ----    
    estado_S.append(X[0])     # salva a posicao
    estado_V.append(X[1])     # salva a velocidade
    estado_Se.append(Xe[0])     # salva a posicao estimada
    estado_Ve.append(Xe[1])     # salva a velocidade estimada
    medida.append(Y)          # salva a medida Y da posicao 
    covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
    tempo.append(t)           # salva o tempo decorrido
    t = t + dt


###################### Figuras ##################################
fig.figure()
fig.plot(tempo,estado_S,color='Black',linewidth=4)
fig.plot(tempo,estado_Se,linestyle='dashed',color='red',linewidth=5)
fig.plot(tempo,medida,color='Black',alpha=0.5)
fig.grid()
fig.xlabel('tempo')
fig.ylabel('posição S(k)')
fig.title('Localização com modelo de estado S(k) e medida com ruído')

fig.figure()
fig.plot(tempo,covP,color='Black',alpha=0.5)

