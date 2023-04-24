# Otimizacao - Programacao Nao Linear
#   Max f(x) = -(x-2)**2
# suj a x >= 3
###################################################
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as fig
from mpl_toolkits import mplot3d

def f(x):
    fx = -(x[0]-2)**2
    return -fx
def restricao(x):
    g = x[0] - 3
    return g

x0=np.array([0])
cons={'type':'ineq','fun':restricao}
res = minimize(f, x0=x0,method='SLSQP',constraints=cons)
###### valores otimos da funcao ####################
print('####### otimizacao ######')
print(' ')
print('valores ótimos de x:',res.x)
print('----------------------------')
print('valor ótimo da função:', -res.fun)






