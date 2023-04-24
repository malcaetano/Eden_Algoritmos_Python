#Otimizacao
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as fig
import numpy as np

#++++++++++ funcao a ser otimizada ++++++
def f(x):
    return x**2 -5*x + 6
#++++++++++ grafico da funcao ++++++++++
x=np.linspace(-1, 6, 100)
fig.plot(x,f(x),'-k',linewidth=5)
fig.xlabel('valores de x', fontsize=14)
fig.ylabel('f(x)', fontsize=14)
fig.title('Otimizacao de f(x)',fontsize=16)
fig.grid()

#+++++ Busca o minimo da funcao ++++++++
res = minimize_scalar(f)
print(res)

