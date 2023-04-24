#Otimizacao
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as fig
import numpy as np

#++++++++++ funcao a ser otimizada ++++++
def f(x):
    return 4*x**3 + 5*(x-2)**2 +x**4

#++++++++++ grafico da funcao ++++++++++
x=np.linspace(-3, 3, 100)
fig.plot(x,f(x),'-k',linewidth=5)
fig.xlabel('valores de x', fontsize=14)
fig.ylabel('f(x)', fontsize=14)
fig.title('Otimizacao de f(x)',fontsize=16)
fig.grid()

#+++++ Busca o minimo da funcao ++++++++
res = minimize_scalar(f)
print(res)
#+++++ raizes da eq. 3o. grau da derivada ########
coef = [4, 12, 10, -20]
raizes= np.roots(coef)
print('++++ coef. da eq. 3o. grau da derivada ++++++++')
print(coef)
print('########### raízes ######################')
print(raizes)
