# Game of Live (Jogo da Vida) - Pulsar
####################################
import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, cm
import random

fig.close('all')  # fecha figuras existentes

n=40              # números de linhas
m=40              # número de colunas

##### inicializa com zeros  ###############
a=np.zeros((n+1,m+1))
novo_a=np.zeros((n+1,m+1))
############################################

######## escolha da estrutura Pulsar ######
a[15,30]=a[15,31]=a[15,32]=1
a[16,30]=a[17,30]=a[18,30]=a[19,30]=1
a[19,31]=a[19,32]=1
a[16,32]=a[17,32]=a[18,32]=1

##############################################

for ger in range(1):    # <----------------- iteração das gerações                        
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
      fig.yticks([])            # esconde os números do eixo y"""
      im = fig.imshow(a, interpolation = "nearest",cmap='Greys',animated=True)
      mgr = fig.get_current_fig_manager()
      mgr.window.setGeometry(20,20,1000, 1000) ## janela fixa
      fig.pause(0.1)                  ### pausa para ver as células se mover

    