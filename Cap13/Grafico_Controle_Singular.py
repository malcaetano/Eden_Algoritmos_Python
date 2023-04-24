import numpy as np
import matplotlib.pyplot as fig

t=np.arange(0,2*np.sqrt(10),0.1)
n=len(t)
y=np.zeros(n)
v=np.zeros(n)
u=np.zeros(n)
for i in range(n):
    if t[i]<np.sqrt(10):
        y[i]=-0.5*t[i]**2+10
        v[i]=-t[i]
        u[i]=0
    else:
        y[i]=0.5*t[i]**2-2*np.sqrt(10)*t[i]+20
        v[i]=t[i]-2*np.sqrt(10)
        u[i]=2

fig.subplot(211)        
fig.plot(t,y,'k-',t,v,'k--')  
fig.ylabel('Variável de estado',fontsize=16)      
fig.legend(['altitude','velocidade'],fontsize=14)
fig.subplot(212)
fig.plot(t,u,'k-')  
fig.ylabel('Controle u(t)',fontsize=16) 