######################################################################
#               Algortimo Genético                                   #  
#               Problema: Valor Minimo de Funcao                     #
######################################################################

import numpy as np
import matplotlib.pyplot as fig

############### inicializacao #####
NCros= 5
ninic = 0
nmax = 10
geracao = 1
tolerancia=10000

L=np.zeros([100,2])
x=np.zeros([100,2])
best=np.ones([100,2])*1000
graf_func=[]
graf_tol=[]

while tolerancia>0.1 and geracao<=20:
  for t in range(NCros):   
    if ninic==0:
        for i in range(nmax):
            L[i,0]=3*np.random.rand(1)
            L[i,1]=L[i,0]**2-5*L[i,0]+6
    else:
        for i in range(1+ninic,nmax*NCros):   
            L[i,0]=L[i-ninic,0]
            L[i,1]=L[i-ninic,1]        
    if geracao==1 or ninic!=0:
        for k in range(1+ninic,nmax*NCros):
            x[k,0]=2*np.random.rand(1)
            x[k,1]=x[k,0]**2-5*x[k,0]+6
        for i in range(nmax*NCros-1):
            for j in range(i+1,nmax*NCros):
                if x[i,1]>=x[j,1]:
                    troca=x[i,0]
                    x[i,0]=x[j,0]
                    x[j,0]=troca
                    troca=x[i,1]
                    x[i,1]=x[j,1]
                    x[j,1]=troca
    r1=abs(np.random.rand(1))                
    f1=int(r1*(nmax*NCros)+1) 
    falt=1.6
    x[f1,0]=x[f1,0]*falt
    x[f1,1]=x[f1,0]**2-5*x[f1,0]+6
    rcr1=abs(0.7*np.random.rand(1))
    fcr1=int(rcr1*(nmax*NCros))+1
    rcr2=abs(0.7*np.random.rand(1))
    fcr2=int(rcr1*(nmax*NCros))+1
    troca=x[fcr1,0]
    x[fcr1,0]=x[fcr2,0]
    x[fcr2,0]=troca
    troca=x[fcr1,1]
    x[fcr1,1]=x[fcr2,1]
    x[fcr2,1]=troca
    x[fcr1,1]=x[fcr1,0]**2-5*x[fcr1,0]+6
    x[fcr2,1]=x[fcr2,0]**2-5*x[fcr2,0]+6
    ninic=ninic+nmax
  print(L[0:10,:])  
  for i in range(nmax*NCros-1):
      for j in range(i+1,nmax*NCros):
          if x[i,1]>x[j,1]:
                    troca=x[i,0]
                    x[i,0]=x[j,0]
                    x[j,0]=troca
                    troca=x[i,1]
                    x[i,1]=x[j,1]
                    x[j,1]=troca
  for j in range(nmax*NCros):
            for i in range(nmax):          
                if x[j,1]<=best[i,1]:
                    for k in range(nmax,i+2,-1):
                               for c in range(2):
                                   best[k,c]=best[k-1,c]
                               for c in range(2):
                                   best[i,c]=x[i,c]
                    i=nmax
  tolerancia=0
  for j in range(1,nmax):
        tolerancia=tolerancia+(abs(best[j,1])-abs(best[j-1,1]))**2    
  tolerancia=np.sqrt(tolerancia)       
  print('geração = ',geracao)
  print('tolerancia = ', tolerancia)
  print('valor função = ',best[0:10,:])  
  graf_func.append(best[0,0])
  graf_tol.append(tolerancia)
  geracao=geracao+1

ax1=fig.subplot(211)
ax1.plot(graf_func,'--ok')
fig.xlabel('Iterações', fontsize=14)
fig.ylabel('Ótimo valor de f(x)', fontsize=16)
ax2=fig.subplot(212)
ax2.plot(graf_tol,'--ok')
fig.xlabel('Iterações', fontsize=14)
fig.ylabel('Tolerância', fontsize=16)