############## EDO DESPOLUICAO #####################
###### Modelo Despoluicao do rio Piracicaba ###########################

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# Condicao Inicial das concentracoes
C10 = 0    # <----------------- poluentes no tanque 1
C20 = 0     # <---------------- poluentes no tanque 2


#Parametros do sistema
alpha = 0.1
beta = 0.2
gamma = 0.3
V1 = 100
V2 = 100
# grade de tempos t
t = np.arange(0, 100, 0.1)

# Sistema de Eq. Diferenciais 
def deriv(s, t, alpha, beta, gamma, V1, V2):
    C1, C2 = s
    c = 1 - np.sin(0.1*t)
    dC1dt = alpha*c - beta*C1
    dC2dt = beta*C1 - gamma*C2
    return dC1dt, dC2dt

# Condicoes iniciais no Vetor
s0 = C10, C20
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(alpha,beta,gamma,V1,V2))
C1, C2 = res.T

# Plot dados X
ax=fig.subplot(211, axisbelow=True)
ax.plot(t, C1, 'k',t,C2,'--k')
ax.set_xlabel('Tempo')
ax.set_ylabel('(C1,   C2)')
fig.grid()
fig.legend(['concentração poluentes C1','concentração poluentes C2'])
fig.tight_layout()


ax=fig.subplot(212, axisbelow=True)
ax.plot(C1, C2, 'k')
ax.set_xlabel('C1(t)')
ax.set_ylabel('C2(t)')
fig.tight_layout()


