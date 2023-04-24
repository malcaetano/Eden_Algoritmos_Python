# fractal da samambaia
import matplotlib.pyplot as fig
from random import randint
# Numero de iterações
n=50000
########### parametros ##################################
a_valor=[0,0.85,0.2,-0.15]
b_valor=[0,0.04,-0.26,0.28]
c_valor=[0,-0.04,0.23,0.26]
d_valor=[0.16,0.85,0.22,0.24]
e_valor=[0,0,0,0]
f_valor=[0,1.6,1.6,0.44]
############## inicializa a lista para fazer o grafico #################
eix=[]
eiy=[]
ax=fig.subplot(111)
############# valores iniciais de x e y
x=0
y=0
############### inicio das repeticoes ################################
for j in range(n):
            p=randint(1,100)   #### sorteio de numero entre 1 e 100
            if p==1:
                a=a_valor[0]
                b=b_valor[0]
                c=c_valor[0]
                d=d_valor[0]
                e=e_valor[0]
                f=f_valor[0]
            elif p<=86:
                a=a_valor[1]
                b=b_valor[1]
                c=c_valor[1]
                d=d_valor[1]
                e=e_valor[1]
                f=f_valor[1]
            elif p<=93:
                a=a_valor[2]
                b=b_valor[2]
                c=c_valor[2]
                d=d_valor[2]
                e=e_valor[2]
                f=f_valor[2]
            elif p<=100:
                a=a_valor[3]
                b=b_valor[3]
                c=c_valor[3]
                d=d_valor[3]
                e=e_valor[3]
                f=f_valor[3] 
            x = a*x+b*y+e     ####### primeira equacao do sistema
            y = c*x+d*y+f     ####### segunda equacao
            eix.append(x)
            eiy.append(y)            

ax.plot(eix,eiy,'.k',markersize=2)    ##### grafico da samambaia
fig.axis('off')


