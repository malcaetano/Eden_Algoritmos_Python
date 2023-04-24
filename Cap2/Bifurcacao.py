# bifurcaçao
import matplotlib.pyplot as fig
import numpy as np

n=1000
iteracao=1000
ultimas=200
r=np.linspace(1,4,n)
x=0.1*np.ones(n)

ax=fig.subplot(111)

for i in range(iteracao):
        x = r*x*(1-x)
        if i>=(iteracao-ultimas):
              ax.plot(r,x,'.k',markersize=2)    

fig.xlabel('Parâmetro r', fontsize=16)
fig.ylabel('x[k]', fontsize=24)


