# Backpropagation para rede neural simples
# Apenas 1 neuronio
############################################

import matplotlib.pyplot as fig

X   = 1.5 # entrada inicial
W0  = 0.8 # peso inicial W
y   = 0.5 # saida desejada para y
r   = 0.1 # taxa de aprendizado

###### bacpropagation baseada na funcao custo C ############
###### Derivada parcial do custo C em relacao aos pesos
###### A previsao yprev = X.W
######  C(y_prev) = (yprev - yreal)**2
######  A derivada parcial :
######  DC/DW = ( DC/Dyprev ) * (Dyprev/DW)
############################################################

def Dc_Dw(y_prev,y,X):
    Dc_Dprev = 2*(y_prev - y)**2
    Dprev_Dw = X
    derivada = Dc_Dprev * Dprev_Dw
    return derivada

W = [ W0 ]
y_prev = [ X*W0 ]

for i in range(0,100):
    y_prev.append(X*W[-1])
    W.append(W[-1] - r*Dc_Dw(y_prev[-1],y,X))
    if (y_prev[-1] - y)**2 < 0.0001:
        break
print(' ')
print('########## resultado final ##########')
print(' Valor desejado na saída da rede Y = ', y)      
print(' Previsão na saída da rede = ', y_prev[-1])
print('+++++++++++++++++++++++++++++++++++++++')
print(' Previsão do peso ótimo W = ',W[-1])    

fig.figure()
fig.subplot(211)
fig.plot(y_prev,'-k')
fig.xlabel('Iterações')
fig.ylabel('Y previsto')
fig.grid()
fig.title('** Convergência para taxa de aprendizagem r = 0.1 **')

fig.subplot(212)
fig.plot(W,'-k')
fig.xlabel('Iterações')
fig.ylabel('Valores do peso W')
fig.grid()

