############## EDO HIV- Aids #####################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
from math import sin, cos, tan, exp, radians, degrees
from mpl_toolkits import mplot3d
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap

# ++++ parâmetros do modelo +++++
s=10       
r=0.52             
Tmax=1700              
mi1=0.4      
mi2=0.5               
mi3=0.03                 
miv=2.4                  
theta=1e6                  
w=1   
beta1=1      
beta2=65470
K10=2.4e-5
K20=0.003
N0=1400

t0=0
tf=365
  
# condicoes inciais - posicao altitude (h)
x10 = 462
# condicoes inciais - longitude (theta)
x20 = 0.027
# condicoes inciais - Latitude (phi)
x30= 0.128
# condicoes inciais - velocidade  (v)
x40 = 0.07121
# vetor do tempo de integracao
t = np.arange(0, tf, 0.1)

# Modelo Dinamico
def deriv(y, t, s,r,Tmax,mi1,mi2,mi3,miv,theta,w,beta1,beta2,K10,K20,N0):
    x1,x2,x3,x4 = y
    S=s*theta/(theta+x4)
    lamb=r*(1-(x1+x2+x3)/Tmax)
    N=beta2-(beta2-N0)*exp(-beta1*t)
    med1=900
    med2=300
    k1=K10*exp(-med1*0.005);
    k2=K20*exp(-med2*0.005);
    dx1dt = S+lamb*x1-x1*(mi1+k1*x4)
    dx2dt = w*k1*x4*x1-x2*(mi2+k2)
    dx3dt = (1-w)*k1*x4*x1+k2*x2-mi3*x3
    dx4dt = N*mi3*x3-x4*(k1*x1+miv)
    return dx1dt, dx2dt, dx3dt, dx4dt

# Condicao Inicial
y0 = x10, x20, x30, x40

# Integrador numerico
ret = odeint(deriv, y0, t, args=(s,r,Tmax,mi1,mi2,mi3,
                                 miv,theta,w,beta1,beta2,
                                 K10,K20,N0))

x1, x2, x3, x4 = ret.T
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fig.subplot(221)
fig.plot(t, x1, '-k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('CD4 não infectada (cel/mm3)', fontsize=10)
fig.tight_layout()
fig.subplot(222)
fig.plot(t, x2, '--k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('CD4 latente(cel/mm3)', fontsize=10)
fig.tight_layout()
fig.subplot(223)
fig.plot(t, x3, '--k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('CD4 ativo (cel/mm3)', fontsize=10)
fig.tight_layout()
fig.subplot(224)
fig.plot(t, x4, ':k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('carga viral (cópias/ml)', fontsize=10)
fig.tight_layout()




