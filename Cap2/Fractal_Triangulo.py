# fractal
import matplotlib.pyplot as fig
import numpy as np
from random import randint
n=1000000
a_valor=[0.5, 0.5, 0.5]
b_valor=[0, 0, 0]
c_valor=[0, 0, 0 ]
d_valor=[0.5, 0.5, 0.5]
e_valor=[0, 0, 0.5]
f_valor=[0, 0.5, 0.5]
eix=[]
eiy=[]
ax=fig.subplot(111)

x=0
y=0
for j in range(n):
            p=randint(1,100)
            if p<=33:
                a=a_valor[0]
                b=b_valor[0]
                c=c_valor[0]
                d=d_valor[0]
                e=e_valor[0]
                f=f_valor[0]
            elif p<=66:
                a=a_valor[1]
                b=b_valor[1]
                c=c_valor[1]
                d=d_valor[1]
                e=e_valor[1]
                f=f_valor[1]
            elif p<=100:
                a=a_valor[2]
                b=b_valor[2]
                c=c_valor[2]
                d=d_valor[2]
                e=e_valor[2]
                f=f_valor[2]
            x = a*x+b*y+e
            y = c*x+d*y+f
            eix.append(x)
            eiy.append(y)            

ax.plot(eix,eiy,'.k',markersize=2)    
fig.axis('off')


