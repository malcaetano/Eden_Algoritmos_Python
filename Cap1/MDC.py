#Algoritmo do max div comum (mdc)
import matplotlib.pyplot as fig

n=int(input("n= "))    # <--- leitura de n 
m=int(input("m= "))    # <--- leitura de m

antigo=n
novo=m
resto = antigo % novo
mdc=[]                  # < --- lista vazia para receber m
while resto !=0:        # <----- repete enquanto resto não nulo
    resto=antigo % novo # <--- divide n/m
    antigo=novo         # <--- m se transforma em n
    novo = resto        # <--- resto se transforma em novo m
    mdc.append(antigo)  # <--- salva m
    
print('++++++++++++  MDC +++++++++++')    
print('MDC(%d,%d) = %d' % (n,m,antigo))    
print(mdc)            

fig.plot(mdc,'-k',linewidth=5)
fig.grid
fig.ylabel('divisores de n e m', fontsize=16)
fig.xlabel('iterações',fontsize=16)
fig.grid()
fig.title('MÁXIMO DIVISOR COMUM - MDC(n,m)', fontsize=16)

