import numpy as np
import cv2
import os 
import glob 
from geneticalgorithm import geneticalgorithm as ga
######## le a matriz ############
img = cv2.imread('Num1.png')
######## salva o formato com elementos [i,j,RGB]
shape=img.shape 
######### transforma imagem em vetor
vetorIm=img.ravel()
######## adiciona ruido na imagem
vetorIm=vetorIm+np.random.rand(len(vetorIm))
######## volta de vetor para matriz              
mat=np.matrix(vetorIm)   
######## usa a forma original para adequar a matriz [i,j,RGB] 
img2=np.asarray(mat).reshape(shape)
####### mostra a imagem
cv2.imshow("Output",img2)

#cv2.imwrite('SaidaF.jpg', im_blend)

