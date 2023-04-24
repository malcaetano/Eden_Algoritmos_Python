import numpy as np
import cv2
import os 
import glob 
import matplotlib.pyplot as fig

from geneticalgorithm import geneticalgorithm as ga


######## le a imagem ############
img = cv2.imread('mona.jpg')
######## salva o formato com elementos [i,j,RGB]
shape=img.shape 
######### transforma imagem em vetor
vetorIm=img.ravel()
######## segunda imagem inicializada
Im_aleat=np.ones(len(vetorIm))

def f(X):
    ff=np.sum(np.abs(X*Im_aleat-vetorIm)**2)
    return ff

algorithm_param = {'max_num_iteration': 100000,\
                   'population_size':15,\
                   'mutation_probability':0.03,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.2,\
                   'parents_portion': 0.25,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

varbound=np.array([[0,255]]*len(vetorIm))

model=ga(function=f,dimension=len(vetorIm),variable_type='int',\
         variable_boundaries=varbound,\
         algorithm_parameters=algorithm_param)

model.run()
######## volta de vetor para matriz    
Im_result=model.best_variable*Im_aleat          
mat=np.matrix(Im_result)   
######## usa a forma original para adequar a matriz [i,j,RGB] 
img2=np.asarray(mat).reshape(shape)
####### mostra a imagem
cv2.imwrite('SaidaF.jpg', img2)


