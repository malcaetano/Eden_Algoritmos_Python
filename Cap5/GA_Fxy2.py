#Algoritmo Genetico - GeneticalAlgorithm
# Instalacao: >> pip install geneticalgorithm
###################################################
# resolvendo a funcao
# f(x,y)=1.5*exp(1/(1+(x-1)**2+(y-1)**2))-2.5*exp(1/(1+
#                 (1/4)*(x+0.5)**2+(1/36)*(y-1)**2))+
#                 2*exp(1/(1+(x-2)**2+(Xy-2)**2))+
#                 2*exp(1/(1+(x-1)**2+(y+1)**2))
#
###################################################
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    ff=1.5*np.exp(1/(1+(X[0]-1)**2+(X[1]-1)**2))-2.5*np.exp(1/(1+\
                 (1/4)*(X[0]+0.5)**2+(1/36)*(X[1]-1)**2))+\
                 2*np.exp(1/(1+(X[0]-2)**2+(X[1]-2)**2))+\
                 2*np.exp(1/(1+(X[0]-1)**2+(X[1]+1)**2))
    return -ff

algorithm_param = {'max_num_iteration': 100,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

varbound=np.array([[-5,5]]*2)

model=ga(function=f,dimension=2,variable_type='real',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()


