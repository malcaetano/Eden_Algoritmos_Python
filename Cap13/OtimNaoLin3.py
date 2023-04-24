# Otimizacao - Programacao Nao Linear
#   max f(x,y) = -(x-4)**2 - (y-4)**2
#   suj a
#       g1: x + y <= 4
#       g2: x + 3y <= 9
#---------------------------------------------------
#O formato no Python deve ser alterado
#      g1: -x-y+4>=0
#      g2: -x-3y+9>=0
##############################################
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as fig
from mpl_toolkits import mplot3d

def f(x):
    fx = -(x[0]-4)**2 - (x[1]-4)**2
    return -fx
def restricao(x):
    g1 = -x[0]-x[1] + 4
    g2 = -x[0] - 3*x[1] + 9 
    return g1, g2

x0=np.array([0, 0])
cons={'type':'ineq','fun':restricao}
res = minimize(f, x0=x0,method='SLSQP',constraints=cons)
###### valores otimos da funcao ####################
print('####### otimizacao ######')
print(' ')
print('valores ótimos de x:',res.x)
print('----------------------------')
print('valor ótimo da função:', -res.fun)

################# grafico da funcao 3D ################
ax=fig.axes(projection='3d')
x1=np.linspace(-4, 10, 100)
y1=np.linspace(-4, 6, 100)
X, Y = np.meshgrid(x1,y1)
Z1=-(X-4)**2 - (Y-4)**2
Z2= X + Y -4
Z3= X + 3*Y - 9
ax.plot_wireframe(X,Y,Z1, color='black', alpha=0.5)
ax.plot_wireframe(X,Y,Z2, color='black', alpha=0.2)
ax.plot_wireframe(X,Y,Z3, color='black', alpha=0.2)
#+++++++++++ titulos dos eixos ++++++++++++++++++++++++
ax.set_xlabel('valores de x', fontsize=14)
ax.set_ylabel('valores de y', fontsize=14)
ax.set_zlabel('f(x,y)',fontsize=14)
fig.title('Otimização de f(x,y)',fontsize=16)
fig.grid()




