######################################################################
#               Algortimo Genético                                   #  
#               Problema: Valor Minimo de Funcao                     #
######################################################################

import numpy as np
import matplotlib.pyplot as fig
#+++++++ Funcao a ser otimizada +++++++++++++
def funcao(a):
    f=a**2-5*a+6
    return f
#+++++++ Funcao para trocar posicoes
def trocalugar(a,b):
    tr=a
    a=b
    b=tr
    return a,b
############### inicializacao #####
NCros= 2        # num de cromossomos
ninic = 0       # contagem inicial de cromossomo
nmax = 10       # quantidade de genes
mutacao=2       # taxa de mutacao entre os genes
crossing=1.6    # taxa de crossing over entre os genes

geracao = 1      # contagem de geracoes
tolerancia=10000 # valor inicial de tolerancia para parada do alg

L=np.zeros([100,2])         # valor inicial dos genes do cromossomo "i"
x=np.zeros([100,2])         # valor modificado dos genes apos 1o. passo
best=np.ones([100,2])*1000  # valor inicial da solucao otima
graf_func=[]     # lista para armazenar valores pontos otimos x*  
graf_xot=[]      # Lista para armazenar valores otimos da funcao f(x*)   
graf_tol=[]      # Lista para armazenar as toletancias das iteracoes

while tolerancia>0.1 and geracao<=20:
  for t in range(NCros):   
    if ninic==0:
        for i in range(nmax):
            L[i,0]=mutacao*np.random.rand(1)
            L[i,1]=funcao(L[i,0])
    else:
        for i in range(1+ninic,nmax*NCros):   
            L[i,0]=L[i-ninic,0]
            L[i,1]=L[i-ninic,1]        
    if geracao==1 or ninic!=0:
        for k in range(1+ninic,nmax*NCros):
            x[k,0]=mutacao*np.random.rand(1)
            x[k,1]=funcao(x[k,0])
        for i in range(nmax*NCros-1):
            for j in range(i+1,nmax*NCros):
                if x[i,1]>=x[j,1]:
                    trocalugar(x[i,0],x[j,0])
                    trocalugar(x[i,1],x[j,1])                 
    r1=abs(np.random.rand(1))                
    f1=int(r1*(nmax*NCros)+1) 
    x[f1,0]=x[f1,0]*crossing
    x[f1,1]=funcao(x[f1,0])
    rcr1=abs(0.7*np.random.rand(1))
    fcr1=int(rcr1*(nmax*NCros))+1
    rcr2=abs(0.7*np.random.rand(1))
    fcr2=int(rcr1*(nmax*NCros))+1
    trocalugar(x[fcr1,0],x[fcr2,0])
    trocalugar(x[fcr1,1],x[fcr2,1])
    x[fcr1,1]=funcao(x[fcr1,0])
    x[fcr2,1]=funcao(x[fcr2,0])
    ninic=ninic+nmax 
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
  print('valor função = ',best[0,:])  
  graf_xot.append(best[0,0])
  graf_func.append(best[0,1])
  graf_tol.append(tolerancia)
  geracao=geracao+1

ax1=fig.subplot(311)
ax1.plot(graf_xot,'--ok')
fig.xlabel('Iterações', fontsize=14)
fig.ylabel('Ótimo ponto x*', fontsize=16)
fig.grid()

ax2=fig.subplot(312)
ax2.plot(graf_func,'--ok')
fig.xlabel('Iterações', fontsize=14)
fig.ylabel('Ótimo da função', fontsize=16)
fig.grid()

ax2=fig.subplot(313)
ax2.plot(graf_tol,'--ok')
fig.xlabel('Iterações', fontsize=14)
fig.ylabel('Tolerância', fontsize=16)
fig.grid()