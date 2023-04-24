# Game of Live (Jogo da Vida) - Gun
####################################
import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, cm
import random

fig.close('all')  # fecha figuras existentes

n=80              # números de linhas
m=80              # número de colunas

##### inicializa com zeros  ###############
a=np.zeros((n+1,m+1))
novo_a=np.zeros((n+1,m+1))
############################################

######## escolha da estrutura Glider Gun ######
a[5,1]=a[5,2]=1
a[6,1]=a[6,2]=1
a[3,13]=a[3,14]=1
a[4,12]=a[4,16]=1
a[5,11]=a[5,17]=1
a[6,11]=a[6,15]=a[6,17]=a[6,18]=1
a[7,11]=a[7,17]=1
a[8,12]=a[8,16]=1
a[9,13]=a[9,14]=1
a[1,25]=1
a[2,23]=a[2,25]=1
a[3,21]=a[3,22]=1
a[4,21]=a[4,22]=1
a[5,21]=a[5,22]=1
a[6,23]=a[6,25]=1
a[7,25]=1
a[3,35]=a[3,36]=1
a[4,35]=a[4,36]=1

##############################################

for ger in range(8):    # <----------------- iteração das gerações                        
      for i in range(1,n): # <-------------- percorre as linhas
           for j in range(1,m): #<---------- percorre as colunas
                vizinho=0
                if a[i-1,j-1]==1:
                           vizinho=vizinho+1                       
                if a[i,j-1]==1:
                           vizinho=vizinho+1                          
                if a[i+1,j-1]==1:
                           vizinho=vizinho+1                       
                if a[i+1,j]==1:
                           vizinho=vizinho+1                       
                if a[i+1,j+1]==1:
                           vizinho=vizinho+1                       
                if a[i,j+1]==1:
                           vizinho=vizinho+1                       
                if a[i-1,j+1]==1:
                           vizinho=vizinho+1                      
                if a[i-1,j]==1:
                           vizinho=vizinho+1                          
                if a[i,j]==1:
                    if (vizinho==2) or (vizinho==3): ### se célula viva com 2
                        novo_a[i,j]=1                ### ou 3 vizinhos, permanece
                    else:                            ### viva
                        novo_a[i,j]=0
                else:
                    if vizinho==3:                  ### se espaço vazio com 2
                       novo_a[i,j]=1                ### ou 3 vizinhos, nasce
                    else:
                       novo_a[i,j]=0                ### se espaço vazio com 1 ou 
      a=novo_a                                      ### 4 viz, permanece vazio
      novo_a=np.zeros((n+1,m+1)) ### atualiza a regra
      fig.title('GERAÇÃO %d' % ger, fontsize=20)
      fig.xticks([])            # esconde os numeros do eixo x
      fig.yticks([])            # esconde os números do eixo y
      im = fig.imshow(a, interpolation = "nearest",cmap='Greys',animated=True)
      mgr = fig.get_current_fig_manager()
      mgr.window.setGeometry(20,20,1000, 1000) ## janela fixa
      fig.pause(0.1)                  ### pausa para ver as células se mover

    