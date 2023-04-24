# Enxame Particulas biblioteca pyswarms
# precisa instalar antes
#>> pip install pyswarms
#############################################

import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history


def f(x):
    return x[:,0]**2-5*x[:,0]+6
# Inicializacao dos Hiperparametros
options = {'c1': 0.5, 'c2': 0.3, 'w':1}

# Chamada da funcao PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=1, options=options)

# Resultado da otimizacao
cost, pos = optimizer.optimize(f, iters=100)

plot_cost_history(cost_history=optimizer.cost_history)

