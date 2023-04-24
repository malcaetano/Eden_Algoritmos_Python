import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
from mpl_toolkits import mplot3d

# Condicao Inicial de x
X0 = 0
# Condicao Inicial de y
Y0 = 1
# Condicao Inicial de z
Z0 = 0

#Parametros do sistema
a = 7.85
b = 24.3
c = 8/3

# grade de tempos t
t = np.linspace(0, 60, 5000)

# Sistema de Eq. Diferenciais de Lorentz
def deriv(s, t, a, b, c):
    X, Y, Z = s
    dXdt = a*(Y - X)
    dYdt = -X*Z + b*X - Y
    dZdt = X*Y - c*Z
    return dXdt, dYdt, dZdt

# Condicoes inciais no Vetor
s0 = X0, Y0, Z0
# Integracao do sistema #########################
res = odeint(deriv, s0, t, args=(a,b,c))
X, Y, Z = res.T

# Plot dados separados X, Y, Z
#plt.figure(facecolor='w')
ax=fig.subplot(311,facecolor='#dddddd', axisbelow=True)
ax.plot(t, X, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('X')

ax=fig.subplot(312,facecolor='#dddddd', axisbelow=True)
ax.plot(t, Y, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('Y')

ax=fig.subplot(313,facecolor='#dddddd', axisbelow=True)
ax.plot(t, Z, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('Z')

fig.figure()
ax2 = fig.axes(projection='3d')
ax2.plot3D(X,Y,Z,'-k')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

