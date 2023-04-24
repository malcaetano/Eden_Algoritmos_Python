######################################################################
#               Algortimo do Enxame de Particulas  2 dimensoes       #
#               Problema: Valor Minimo de Funcao                     #
######################################################################
import numpy as np
import matplotlib.pyplot as fig
############### geracao das particulas iniciais e suas velocidades #####
n_partic=10
x=np.random.rand(n_partic,2)
v=np.random.rand(n_partic,2)
p=x
############### parametros de cognicao e socializacao #################
fi1=0.5     # -------> cognicao
fi2=0.5     # -------> socializacao
############## chute inicial para o otimo global e local ##############
FFbest=100000
FF=np.zeros(n_partic)
FP=np.zeros(n_partic)
ax=fig.subplot(111)
########### calculos iniciais das projecoes para x(k) e v(k) ######
for i in range(n_partic):
        FF[i]=p[i,0]**2 + p[i,1]**2
        p[i,0]=x[i,0]
        p[i,1]=x[i,1]
        if FF[i]<FFbest:
              FFbest=FF[i]
              g1=p[i,0]
              g2=p[i,1]
##################### parte do algoritmo para busca do valor otimo #####
#########################################################################         
k=1
erro=1000
while erro>0.01:
    if k>100:
        erro=0
    else:
        for i in range(n_partic):
                v1=v[i,0]+(fi1*np.random.rand())*(p[i,0]-x[i,0])+\
                (fi2*np.random.rand())*(g1-x[i,0])
                v2=v[i,1]+(fi1*np.random.rand())*(p[i,1]-x[i,1])+\
                (fi2*np.random.rand())*(g2-x[i,1])
                x1=x[i,0]+v1
                x2=x[i,1]+v2
                FF[i]=x[i,0]**2 + x[i,1]**2
                p[i,0]=x[i,0] 
                p[i,1]=x[i,1]  
                if FF[i]<FFbest:
                    FFbest=FF[i]
                    g1=p[i,0]
                    g2=p[i,1]
                x[i,0]=x1
                x[i,1]=x2
                v[i,0]=v1
                v[i,1]=v2
        ax.plot(x[:,0],x[:,1],'.k')            
        fig.pause(0.1)
        erro=abs(FFbest)
    k=k+1
    print(k)
############################ fim da iteracao ######################
#   melhores pontos, que convergiram e deram o menor erro entre a
#   funcao e os dados reais serao g1
###################################################################    
ax.plot(g1,g2,'*r', markersize=15)
print(g1,g2,FFbest)   

