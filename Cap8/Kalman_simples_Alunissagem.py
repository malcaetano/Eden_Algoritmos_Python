### MODULO LUNAR - ALUNISSAGEM
# Filtro de Kalman
######################################################
import numpy as np
import matplotlib.pyplot as fig
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
X=np.array([[100], [0], [0], [0]])     # <--- alt, dist e veloc iniciais "reais"
Xe=np.array([[90],[0], [0], [0]])      # <--- inicializacao das estimativas
dt=0.1                      # <--- incremento no tempo

################### Matrizes do Modelo ######################
A=np.array([[1, dt, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, dt],
            [0, 0, 0, 1]])   # <------- Modelo posicao e veloc

B=np.array([[0],
            [0],
            [dt**2],
            [2*dt]])   # <------- Matriz do angulo de descida

C=np.identity(4)      # indica que o sensor é mede todas as variaveis

theta=0.1                 # <--- valor do angulo de descida constante

################### Ruidos #################################
desv_1=0.05             # < ---- ruido da altitude
desv_2=0.05             # < ---- ruido na velocidade vertical
desv_3=0.05             # < ---- ruido na distancia horizontal
desv_4=0.05             # < ---- ruido na velocidade horizontal
desv_y=1                # ruido na medida dos sensores

################## Matrizes de Covariancia #############
                # Covariancia do ruido do estado
Q=np.array([[desv_1**2,0,0,0],
            [0,desv_2**2,0,0],
            [0, 0, desv_3**2, 0],
            [0,0,0,desv_4**2]])

                # Covariancia do ruido de medida para todas as variáveis
R=desv_y**2*np.identity(4)
#######################################################
#     Equacao da medida do sensor
#----------------------------------------------               
Psi=np.sqrt(desv_y**2) * np.random.randn(1)*np.ones(4)
Y = np.matmul(C,X) + Psi[:,np.newaxis]  
######################################################

P = Q                       # covariancia inicial

# Simulacao do Movimento +++++++++++++++++++++++++++
t = 0
tfinal=30

estado_S.append(X[0])     # salva a altitude
estado_V.append(X[2])     # salva a distancia horizontal x(k)
estado_Se.append(Xe[0])     # salva a altitude estimada
estado_Ve.append(Xe[2])     # salva a distancia horizontal x(k) estimada
medida.append(Y[0])          # salva a medida Y da altitude
covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
tempo.append(t)           # salva o tempo decorrido
    
while t<=tfinal:
    w1 = np.random.randn(1)   # var aleatoria normal(0,1)
    w2 = np.random.randn(1)   # var aleatoria normal(0,1)
    w3 = np.random.randn(1)   # var aleatoria normal(0,1)
    w4 = np.random.randn(1)   # var aleatoria normal(0,1)
# ---------------- geracao do ruido de altitude, dist. horizontal e veloc ----    
    W=np.matmul(np.sqrt(Q),np.array([w1,w2,w3,w4])) 
#----------------- modelo de estado com ruido -------------------    
    X = np.matmul(A,X) + B*theta + W 
#---------------- modelo de estado estimado -------------------
    Xe = np.matmul(A,Xe) + B*theta 
#----------------- covariancia do estado -----------------
    P = np.matmul(np.matmul(A,P),np.transpose(A)) + np.matmul(np.matmul(C,Q),np.transpose(C))    
#----------------- estimador do sensor de medida ------------
    Z = np.matmul(C,Xe)   
#---------------- modelo da medida com ruido ------------------    
    Psi=np.sqrt(desv_y**2) * np.random.randn(1)*np.ones(4)
    Y = np.matmul(C,X) + Psi[:,np.newaxis]  

###################################################################
###### Filtro de Kalman #############################################
# +++++ ganho K
    k1= np.matmul(P,np.transpose(C))
    k2= np.matmul(np.matmul(C,P),np.transpose(C)) + R
    K = np.matmul(k1,inv(k2))
    Xe = Xe + np.matmul(K,(Y-Z)) 
    p1 = P
    p2 = inv(np.identity(len(Q)) + np.matmul(K,C))
    P = np.matmul(p1,p2)
#----------------- salvando os valores em lista para figuras ----    
    estado_S.append(X[0])     # salva a altitude
    estado_V.append(X[2])     # salva a distancia horizontal
    estado_Se.append(Xe[0])     # salva a altitude estimada
    estado_Ve.append(Xe[2])     # salva a distancia horizontal estimada
    medida.append(Y[0])          # salva a medida Y da altitude 
    covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
    tempo.append(t)           # salva o tempo decorrido
    t = t + dt


###################### Figuras ##################################
fig.figure()
fig.plot(tempo,estado_S,color='Black',linewidth=4)
fig.plot(tempo,estado_Se,linestyle='dashed',color='red',linewidth=3)
fig.plot(tempo,medida,color='Black',alpha=0.5)
fig.grid()
fig.xlabel('tempo')
fig.ylabel('altitude y(k)')
fig.title('Altitude Y(k) e medida com ruído')

fig.figure()
fig.plot(estado_V,estado_S,color='Black',linewidth=4)
fig.xlabel('distância horizontal x(k)')
fig.ylabel('altitude y(k)')
fig.title('Trajetória da alunissagem (distancia horiz, altitude)')

fig.figure()
fig.plot(tempo,covP,color='Black',alpha=0.5)
fig.ylabel('Covariância P(0,0)')
