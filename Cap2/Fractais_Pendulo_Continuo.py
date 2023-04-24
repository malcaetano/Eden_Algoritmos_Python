import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
import math as mt

# Condicao Inicial de x
#X0 = 0
# Condicao Inicial de y
#Y0 = 1

# grade de tempos t
t = np.linspace(0, 20, 100)

# Sistema de Eq. Diferenciais de Lorenz
def deriv(s, t):
    X, Y = s
    dXdt = Y
    dYdt = -0.15*Y + 0.5*X*(1-X**2) + 0.1*mt.cos(t*0.833)
    return dXdt, dYdt

# Condicoes inciais no Vetor
n=3000
XI=np.linspace(-2.4,2.4,n)    
YI=np.linspace(-1.2,1.2,n)
eix=[]
eiy=[]
for i in range(n):
    X0=XI[i]
    for j in range(n):
        Y0=YI[j]
        s0 = X0, Y0
        # Integracao do sistema #########################
        res = odeint(deriv, s0, t)
        X, Y = res.T
    eix.append(X[-1])
    eiy.append(Y[-1])
    print('#########   ',i)

fig.plot(eix,eiy,'.k')




