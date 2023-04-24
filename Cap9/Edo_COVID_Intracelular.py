############## EDO Covid-19 Intracelular #####################
##############  Modelo Sars-Cov-2   ###########################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as m

# Partículas virais iniciais V(t).
V0 = 1e5
# Células de defesa CD4
T0 = 1e8
# Inflamações iniciais
I0=0.01

# ++++ parâmetros do modelo +++++

p, ct, c = 5.2, 1e-9, 9e-1
deltaT, r, K, kt = 1e-2, 2, 1e9, 3.8e8
epson, delta, w, ro = 1, 10, 1, 2

# vetor do tempo de integracao
t = np.linspace(0, 20, 40)

# Modelo Dinamico
def deriv(y, t, p, ct, c, deltaT, r, K, kt, epson, delta, w, ro):
    V, T, I = y
    dVdt = p*V*(1-V/K)-ct*V*T-c*V
    dTdt = r*T*(V**2/(V**2+kt**2))-deltaT*T
    dIdt = epson*(1+m.tanh((m.log10(T)-delta)/w))-ro*m.log10(I)
    return dVdt, dTdt, dIdt

# Condicao Inicial
y0 = V0, T0, I0

# Integrador numerico
ret = odeint(deriv, y0, t, args=(p, ct, c, deltaT, r, K, kt, epson, delta, w, ro))
V, T, I = ret.T

# ++++++ medida dos sintomas da covid-19 ++++++++++++++++++++++++++
S=0.5*np.log10(V)+I
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ax=plt.subplot(111,axisbelow=True)
#ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, V, '-k', linewidth=2, lw=2, label='V(t) Patogeneicidade')
ax.plot(t, T, '--k',linewidth=2, lw=2, label='T(t) Defesa Imune')
ax.plot(t, I, ':k', linewidth=5, lw=2, label='I(t) Inflamação')

ax.set_xlabel('tempo',fontsize=16)
ax.set_ylabel('(V,  T,  I)', fontsize=16)
ax.set_yscale('log')

ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, alpha=0.2, which='major', c='k', lw=2, ls='--')

ax2=ax.twinx()

ax2.plot(t, S, '-ok', lw=2, label='Sintomas')
ax2.set_ylabel('Sintomas da Covid-19 ( S )',fontsize=16)
legend = ax.legend(fontsize=18)
legend.get_frame().set_alpha(0.8)

legend = ax2.legend(fontsize=18)
legend.get_frame().set_alpha(0.8)

