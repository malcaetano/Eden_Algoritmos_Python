#Algoritmo Genetico - GeneticalAlgorithm
# Instalacao: >> pip install geneticalgorithm
###################################################
# resolvendo a funcao
# yLin=beta0+betax
#
###################################################
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    ff=0
    for i in range(len(col1)):
         ff=ff+(col2[i]-X[0]-X[1]*col1[i])**2 
    return ff

algorithm_param = {'max_num_iteration': 100,\
                   'population_size':100,\
                   'mutation_probability':0.05,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}
col1=[0,0.5,1,2,3,4,5]
col2=[5,1,2,4,6,8,10]
varbound=np.array([[0,5]]*2)

model=ga(function=f,dimension=2,variable_type='real',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()


