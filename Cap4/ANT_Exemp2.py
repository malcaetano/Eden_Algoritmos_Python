# Algoritmo Colonia de Formigas
import pants
import math
import random
import matplotlib.pyplot as fig
import numpy as np


##### Parameters:	
#       alpha (float) – relative importance of pheromone (default=1)
#       beta (float) – relative importance of distance (default=3)
#       rho (float) – percent evaporation of pheromone (0..1, default=0.8)
#       q (float) – total pheromone deposited by each Ant after each iteration is complete (>0, default=1)
#       t0 (float) – initial pheromone level along each Edge of the World (>0, default=0.01)
#       limit (int) – number of iterations to perform (default=100)
#       ant_count (float) – how many Ants will be used (default=10)
#       elite (float) – multiplier of the pheromone deposited by the elite Ant (default=0.5)
######################################################################

nodes=list(range(5))
ptos=[(3.5,5),(6,3),(1,3),(2,1),(5,1)]
pesos=np.array([[0,22,50,48,29],
                [22,0,30,34,32],
                [50,30,0,22,23],
                [48,34,22,0,35],
                [29,32,23,35,0]])
arestas=['A','B','C','D','E']   
def custo(a,b):  
    return pesos[a][b] 

world=pants.World(nodes,custo)

solver=pants.Solver(rho=0.5,q=1,t0=0.01,limit=50,ant_count=10)

solution=solver.solve(world)
print(solution.distance)
print(solution.tour)
rota=solution.tour

print('###################')
for i in range(len(rota)):
    print(arestas[rota[i]])


########### figura ###############

x=[]
y=[]
ax=fig.subplot(111) 
for i in range(5):
       x.append(ptos[rota[i]][0])
       y.append(ptos[rota[i]][1])
       ax.text(ptos[i][0],ptos[i][1],s=arestas[i],fontsize=20)

x.append(ptos[rota[0]][0])
y.append(ptos[rota[0]][1])      

ax.plot(x,y,'--k')
ax.plot(x,y,'ok',markersize=6)
ax.plot(x[0],y[0],'og',markersize=10)
ax.axis('off')


