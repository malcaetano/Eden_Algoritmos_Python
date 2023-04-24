import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# Condicao Inicial de x
X10 = 1
X20 = 0
#Parametros do sistema
a = -1
# grade de tempos t
t = np.arange(0, 7, 0.05)

# Sistema de Eq. Diferenciais 
def deriv(s, t, a):
    X1, X2= s
    dX1dt = X2
    dX2dt = a*X1
    return dX1dt, dX2dt

# Condicoes iniciais no Vetor
s0 = X10, X20
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(a,))
X1, X2= res.T

# Plot dados X
ax=fig.subplot(311, axisbelow=True)
ax.plot(t, X1, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('X1')
fig.grid()
fig.tight_layout()

ax=fig.subplot(312, axisbelow=True)
ax.plot(t, X2, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('X2')
fig.grid()
fig.tight_layout()

ax=fig.subplot(313, axisbelow=True)
ax.plot(X1, X2, 'k')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
fig.tight_layout()


