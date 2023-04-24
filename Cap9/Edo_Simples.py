import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# Condicao Inicial de x
X0 = 1
#Parametros do sistema
a = -1
# grade de tempos t
t = np.arange(0, 1, 0.05)

# Sistema de Eq. Diferenciais 
def deriv(s, t, a):
    X= s
    dXdt = a*X
    return dXdt

# Condicoes iniciais no Vetor
s0 = X0
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(a,))
X, = res.T

# Plot dados X
ax=fig.subplot(111, axisbelow=True)
ax.plot(t, X, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('X')
fig.grid()



