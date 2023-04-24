############## EDO SIR #####################
###### Modelo Epidemiológico ###########################

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# Condicao Inicial de x
S0 = 100    # <--------------- suscetíveis
I0 = 2     # <---------------- infectados
R0 = 2     # <---------------- recuperados

#Parametros do sistema
beta = 0.01
gamma = 0.2
# grade de tempos t
t = np.arange(0, 20, 0.1)

# Sistema de Eq. Diferenciais 
def deriv(s, t, beta, gamma):
    S, I, R= s
    dSdt = -beta*S*I
    dIdt = beta*S*I - gamma*I
    dRdt = gamma*I
    return dSdt, dIdt, dRdt

# Condicoes iniciais no Vetor
s0 = S0, I0, R0
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(beta,gamma))
S, I, R= res.T

# Plot dados X
ax=fig.subplot(211, axisbelow=True)
ax.plot(t, S, 'k',t,I,'--k',t,R,':k', markersize=3)
ax.set_xlabel('Tempo')
ax.set_ylabel('(S,I,R)')
fig.grid()
fig.legend(['susceptíveis','infectados', 'recuperados'])
fig.tight_layout()


ax=fig.subplot(212, axisbelow=True)
ax.plot(S, I, 'k')
ax.set_xlabel('Susceptíveis')
ax.set_ylabel('Infectados')
fig.tight_layout()


