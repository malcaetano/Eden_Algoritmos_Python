#Algoritmo Genetico - GeneticalAlgorithm
# Instalacao: >> pip install geneticalgorithm
###################################################
# resolvendo a funcao
# f(x,y)=x*sin(4x)+1.1*y*sin(2y)
###################################################
import numpy as np
import math as mt
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    ff=X[0]*mt.sin(4*X[0])+1.1*X[1]*mt.sin(2*X[1])
    return ff

algorithm_param = {'max_num_iteration': 100,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

varbound=np.array([[0,10]]*2)

model=ga(function=f,dimension=2,variable_type='real',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()


