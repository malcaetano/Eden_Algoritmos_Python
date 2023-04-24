### Balao de ar quente
# Filtro de Kalman
######################################################
import numpy as np
import matplotlib.pyplot as fig
from numpy.linalg import inv

####### inicializacao das listas para armazenar os dados
estado_X=[]
estado_Y=[]
estado_Xe=[]
estado_Ye=[]
medida=[]
covP=[]
tempo=[]


##############################################################
X=np.array([[20], [10] ])     # <--- v e T iniciais "reais"
Xe=np.array([[0], [0] ])      # <--- inicializacao das estimativas
dt=0.1                      # <--- incremento no tempo

################### Matrizes do Modelo ######################
A=np.array([[1-0.25*dt, 0.25*dt], 
            [0, 1-0.2*dt]])   # <------- Modelo discreto de x e y

B=np.array([[0],
            [dt]])   # <------- Matriz do calor de entrada 

C=np.identity(2)      # indica que o sensor mede as 2 variaveis x e y

du=20               # fluxo do calor de entrada (controle)
################### Ruidos #################################
desv_1=1             # < ---- perturbação na velocidade
desv_2=1             # < ---- perturbação na chama de calor

desv_y=3                # ruido na medida do sensor

################## Matrizes de Covariancia #############
                # Covariancia do ruido do estado
Q=np.array([[desv_1**2,0],
            [0,desv_2**2]])

                # Covariancia do ruido de medida para todas as variáveis
R=desv_y**2*np.identity(2)
#######################################################
#     Equacao da medida do sensor
#----------------------------------------------               
Psi=np.sqrt(desv_y**2) * np.random.randn(1)*np.ones(2)
Y = np.matmul(C,X) + Psi[:,np.newaxis]  
######################################################

P = Q                       # covariancia inicial

# Simulacao do Movimento +++++++++++++++++++++++++++
t = 0
tfinal=10

estado_X.append(X[0])     # salva x(k)
estado_Y.append(X[1])     # salva y(k)
estado_Xe.append(Xe[0])     # salva x estimado
estado_Ye.append(Xe[1])     # salva y estimado
medida.append(Y[0])          # salva a medida x do sensor
covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
tempo.append(t)           # salva o tempo decorrido
    
while t<=tfinal:
    w1 = np.random.randn(1)   # var aleatoria normal(0,1)
    w2 = np.random.randn(1)   # var aleatoria normal(0,1)
# ---------------- geracao do ruido de altitude, dist. horizontal e veloc ----    
    W=np.matmul(np.sqrt(Q),np.array([w1,w2])) 
#----------------- modelo de estado com ruido -------------------    
    X = np.matmul(A,X) + B*du + W 
#---------------- modelo de estado estimado -------------------
    Xe = np.matmul(A,Xe) + B*du 
#----------------- covariancia do estado -----------------
    P = np.matmul(np.matmul(A,P),np.transpose(A)) + np.matmul(np.matmul(C,Q),np.transpose(C))    
#----------------- estimador do sensor de medida ------------
    Z = np.matmul(C,Xe)   
#---------------- modelo da medida com ruido ------------------    
    Psi=np.sqrt(desv_y**2) * np.random.randn(1)*np.ones(2)
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
    estado_X.append(X[0])     # salva x(k)
    estado_Y.append(X[1])     # salva y(k)
    estado_Xe.append(Xe[0])     # salva x(k) estimado
    estado_Ye.append(Xe[1])     # salva y(k)estimado
    medida.append(Y[0])          # salva a medida X do sensor 
    covP.append(P[0][0])      # salva o elemento (0,0) da mat Cov
    tempo.append(t)           # salva o tempo decorrido
    t = t + dt


###################### Figuras ##################################
fig.figure()
fig.plot(tempo,estado_X,color='Black',linewidth=4)
fig.plot(tempo,estado_Xe,linestyle='dashed',color='red',linewidth=3)
fig.plot(tempo,medida,color='Black',alpha=0.5)
fig.grid()
fig.xlabel('tempo')
fig.ylabel('velocidade do balão v(k)')
fig.title('velocidade do balão v(k) e medida com ruído')

fig.figure()
ax=fig.subplot(111)
ax.plot(estado_X,estado_Y,color='Black',linewidth=4)
ax.plot(estado_Xe,estado_Ye,color='Black',linewidth=2,linestyle='--')
#ax.set_ylim(-0.2,1)
fig.grid()
ax.set_xlabel('velocidade v(k)')
ax.set_ylabel('temperatura T(k)')
fig.title('velocidade x temperatura')

fig.figure()
fig.plot(tempo,covP,color='Black',alpha=0.5)
fig.ylabel('Covariância P(0,0)')
