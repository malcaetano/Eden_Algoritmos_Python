############## EDO PREDADOR X PRESA #####################
###### Modelo Lotka-Volterra ###########################

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# Condicao Inicial de x
X10 = 100    # <--------------- presa
X20 = 40     # <--------------- predador
#Parametros do sistema
a = 0.5
b = 0.01
c = 0.5
d = 0.01
# grade de tempos t
t = np.arange(0, 20, 0.1)

# Sistema de Eq. Diferenciais 
def deriv(s, t, a):
    X1, X2= s
    dX1dt = a*X1 - b*X1*X2
    dX2dt = -c*X2 + d*X1*X2
    return dX1dt, dX2dt

# Condicoes iniciais no Vetor
s0 = X10, X20
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(a,))
X1, X2= res.T

# Plot dados X
ax=fig.subplot(211, axisbelow=True)
ax.plot(t, X1, 'k',t,X2,'--k')
ax.set_xlabel('Tempo')
ax.set_ylabel('(X1, X2)')
fig.grid()
fig.legend(['PRESA','PREDADOR'])
fig.tight_layout()


ax=fig.subplot(212, axisbelow=True)
ax.plot(X1, X2, 'k')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
fig.tight_layout()


