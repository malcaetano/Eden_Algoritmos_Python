#Algoritmo Genetico - GeneticalAlgorithm
# Instalacao: >> pip install geneticalgorithm
###################################################
# resolvendo a funcao
# y = f(x)=x**2-5x+6
###################################################
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    ff=X[0]**2-5*X[0]+6
    return ff

algorithm_param = {'max_num_iteration': 10,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

varbound=np.array([[0,5]])

model=ga(function=f,dimension=1,variable_type='real',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()
