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
      s=0            # <----------- inicializa a contagem de células vivas 
      for i in range(n):
          for j in range(n):
              s=s+a[i,j]          # <------ conta quantas células vivas existem
      cont=cont+1                 # <------ atualiza a geração
      vivo[cont]=s                # <------ salva no vetor o número de vivas
      fig.figure(2)  
      fig.title('GERAÇÃO %d' % cont, fontsize=20)
      fig.plot(vivo[:cont],'-k')  #<------- atualiza a figura com nu. vivas
      fig.xlabel('GERAÇÃO', fontsize=12)
      fig.ylabel('POPULAÇÃO',fontsize=20)
      mgr = fig.get_current_fig_manager()
      mgr.window.setGeometry(800,20,1000, 500)
      fig.pause(0.1)
      return im

################### tamanho da matriz do jogo nxn  
n=80 
################## cria um vetor para salvar qtde de células vivas por geração
vivo=np.zeros(300)
################## cria a matriz do jogo com zeros de ordem nxn
a=np.zeros((n+1,n+1))
################# inicializa a estrutura do jogo ####################
################# célula viva = 1 
################# célula morta = 0
####################################################################
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

    