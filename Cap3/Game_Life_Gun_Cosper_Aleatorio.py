# Game of Live (Jogo da Vida) - Glider Gun
####################################
import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation
import random
################ function que define as regras do jogo ##################
def update(data):
      global a
      global cont
      novo_a=np.zeros((n+1,n+1))  # <--------zera a matriz da proxima geração
      for i in range(1,n):
           for j in range(1,n):
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
                    if (vizinho==2) or (vizinho==3):
                        novo_a[i,j]=1
                    else:
                        novo_a[i,j]=0
                else:
                    if vizinho==3:
                       novo_a[i,j]=1
                    else:
                       novo_a[i,j]=0
      a=novo_a       # <----------- faz a matriz da geração anterior ser atual
      im.set_data(a) # <----------- atualiza os dados da imagem
      cont=cont+1                 # <------ atualiza a geração
      fig.figure(2)  
      fig.title('GERAÇÃO %d' % cont, fontsize=20)
      fig.axis('off')
      mgr = fig.get_current_fig_manager()
      mgr.window.setGeometry(777,30,300, 400)
      fig.pause(0.01)
      return im

################### tamanho da matriz do jogo nxn  
n=100 
################## cria a matriz do jogo com zeros de ordem nxn
a=np.zeros((n+1,n+1))

for i in range(n):
      for j in range(n):
          w=random.gauss(0,1)
          if w>1:
              a[i,j]=1
          else:
              a[i,j]=0
################# inicializa a estrutura do jogo ####################
################# célula viva = 1 
################# célula morta = 0
####################################################################
"""a[5,1]=a[5,2]=1
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

#++++++++++++++++++++++++++ segundo glider gun ++++++++++++++++++++++++++++++

a[50,3]=a[50,4]=a[51,3]=a[51,4]=1
a[61,1]=a[61,2]=a[61,6]=a[61,7]=1
a[63,2]=a[63,6]=1
a[64,3]=a[64,4]=a[64,5]=1
a[65,3]=a[65,4]=a[65,5]=1
a[68,6]=1
a[69,5]=a[69,6]=a[69,7]=1
a[70,4]=a[70,8]=1
a[71,6]=1
a[72,3]=a[72,9]=1
a[73,3]=a[73,9]=1
a[74,4]=a[74,8]=1
a[75,5]=a[75,6]=a[75,7]=1
a[84,5]=a[84,6]=1
a[85,5]=a[85,6]=1
###################################################################
#++++++++++++++++++++++++++ terceiro glider gun ++++++++++++++++++++++++++++++

a[95,50]=a[95,51]=a[94,50]=a[94,51]=1
a[97,61]=a[96,61]=1
a[91,61]=a[92,61]=1

a[92,63]=a[96,63]=1

a[93,64]=a[93,65]=a[94,64]=a[94,65]=a[95,64]=a[95,65]=1
a[92,68]=1

a[91,69]=a[92,69]=a[93,69]=1

a[90,70]=a[94,70]=1

a[92,71]=1

a[89,72]=a[89,73]=a[95,72]=a[95,73]=1

a[90,74]=a[94,74]=1
a[91,75]=a[92,75]=a[93,75]=1
a[92,84]=a[92,85]=a[93,84]=a[93,85]=1"""

###################################################################
############ faz a animação dos jogos com atualização da function ####

cont=0
figura, ax=fig.subplots()
ax.axis('off')
im = ax.imshow(a, interpolation = "nearest",cmap='Greys', animated=True)
mgr = fig.get_current_fig_manager()
mgr.window.setGeometry(20,20,500, 500)
anima=animation.FuncAnimation(figura, update, interval=20,save_count=50)
fig.show()

    