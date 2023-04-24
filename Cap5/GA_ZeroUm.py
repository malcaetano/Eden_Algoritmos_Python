import numpy as np
import cv2
import os 
import glob 
import matplotlib.pyplot as fig

from geneticalgorithm import geneticalgorithm as ga


######### transforma imagem em vetor
vetorIm=[10,10,10,0,0,0,10,10,10,10]
######## segunda imagem iniciaçlizada
Im_aleat=np.ones(len(vetorIm))*10

def f(X):
    ff=np.sum(np.abs(X*Im_aleat-vetorIm))
    return ff

algorithm_param = {'max_num_iteration': 10,\
                   'population_size':10,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

varbound=np.array([[0,1]]*len(vetorIm))

model=ga(function=f,dimension=len(vetorIm),variable_type='int',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()
Im_result=model.best_variable*Im_aleat 
print(Im_result)