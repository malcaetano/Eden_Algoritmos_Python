# Otimizacao - Programacao Nao Linear
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as fig
from mpl_toolkits import mplot3d

def f(x):
    fx = x[0]**3+3*x[0]*x[1]**2-15*x[0]-12*x[1]
    return fx

x0=np.array([0,0])
res = minimize(f, x0=x0,method='SLSQP')
###### valores otimos da funcao ####################
print('####### otimizacao ######')
print(' ')
print('valores ótimos de x:',res.x)
print('----------------------------')
print('valor ótimo da função:', -res.fun)


ax=fig.axes(projection='3d')
x1=np.linspace(-4, 4, 100)
y1=np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x1,y1)
Z=X**3+3*X*Y**2-15*X-12*Y
ax.plot_wireframe(X,Y,Z, color='black', alpha=0.5)

ax.set_xlabel('valores de x', fontsize=14)
ax.set_ylabel('valores de y', fontsize=14)
ax.set_zlabel('f(x,y)',fontsize=14)
fig.title('Otimização de f(x,y)',fontsize=16)
fig.grid()




