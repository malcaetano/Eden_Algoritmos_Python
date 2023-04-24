# Enxame Particulas biblioteca pyswarms
# precisa instalar antes
#>> pip install pyswarms
# FUNCAO DE ROSENBROCK
#############################################

import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import numpy as np

def f(x):
    return (1 - x[:,0])**2 + 100*(x[:,1] - x[:,0]**2 )**2
# Inicializacao dos Hiperparametros
options = {'c1': 0.5, 'c2': 0.3, 'w':1}

# Chamada da funcao PSO
x_max = 3*np.ones(2)
x_min = -1*x_max
bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(n_particles=10, 
                                    dimensions=2, 
                                    options=options, 
                                    bounds=bounds)

# Resultado da otimizacao
cost, pos = optimizer.optimize(f, iters=100)

plot_cost_history(cost_history=optimizer.cost_history)

