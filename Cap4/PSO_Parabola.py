######################################################################
#               Algortimo do Enxame de Particulas                    #
#               Problema: Valor Minimo de Funcao                     #
######################################################################

import numpy as np
import matplotlib.pyplot as fig

############### geracao das particulas iniciais e suas velocidades #####
n_partic=20
x=np.random.rand(n_partic,1)
v=np.random.rand(n_partic,1)
t=np.arange(0,5,0.1)
ft=t**2 - 5*t + 6
p=x
############### eixo dos gráficos fixos em (-20,20) ###################
ax=fig.subplot(111)
ax.plot(t,ft,'--b')
fig.xlabel('x')
fig.ylabel('f(x)')
############### parametros de cognicao e socializacao #################
fi1=0.5     # -------> cognicao
fi2=0.5     # -------> socializacao
############## chute inicial para o otimo global e local ##############
FFbest=1000

FF=np.zeros(n_partic)
FP=np.zeros(n_partic)
########### calculos iniciais das projecoes para x(k) e v(k) ######
for i in range(n_partic):
        FF[i]=x[i,0]**2 - 5*x[i,0] + 6
        p[i,0]=x[i,0]

for i in range(n_partic):
        FP[i]=p[i,0]**2 -5*p[i,0] + 6
        if FP[i]<FFbest:
              FFbest=FP[i]
              g1=p[i,0]

##################### parte do algoritmo para busca do valor otimo #####
#                    nesse caso o otimo eh aquele onde os parametros
#                    nao se alteram e os valores da funcao em comparacao
#                    com os dados reais a cada tempo t, sao os menores
#                    possiveis
#########################################################################         
k=1
erro=1000
while erro>0.01:
    if k>100:
        erro=0
    else:
        for i in range(n_partic):
                v[i,0]=v[i,0]+(fi1*np.random.rand())*(p[i-1,0]-x[i-1,0])+\
                (fi2*np.random.rand())*(g1-x[i-1,0])
                x[i,0]=x[i-1,0]+v[i-1,0]
                FF[i]=x[i-1,0]**2 -5*x[i-1,0] + 6
                p[i,0]=x[i,0]  
                ax.plot(x[:,0],FF,'.k')
                fig.pause(0.1)
        for i in range(n_partic):
               FP[i]=p[i,0]**2 -5*p[i,0] + 6
               if FP[i]<FFbest:
                    FFbest=FP[i]
                    g1=p[i,0]
        ax.plot(g1,FFbest,'*r', markersize=15)
        fig.pause(0.1)
        erro=FFbest
        print(g1)
    k=k+1
    print(k)
############################ fim da iteracao ######################
#   melhores pontos, que convergiram e deram o menor erro entre a
#   funcao e os dados reais serao g1
###################################################################    
print(g1,FFbest)   
