# Algoritmo Colonia de Formigas
import pants
import matplotlib.pyplot as fig
import numpy as np


nodes=list(range(4))
ptos=[(1,1),(1,3),(3,3),(3,1)]
pesos=np.array([[0,5,9,6],
                [5,0,4,7],
                [9,4,0,3],
                [6,7,3,0]])
arestas=['A','B','C','D']   
def custo(a,b):  
    return pesos[a][b] 

world=pants.World(nodes,custo)

solver=pants.Solver(rho=0.5,q=1,t0=1,limit=50,ant_count=10)

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
for i in range(4):
       x.append(ptos[rota[i]][0])
       y.append(ptos[rota[i]][1])
       ax.text(ptos[i][0],ptos[i][1],s=arestas[i],fontsize=20)

x.append(ptos[rota[0]][0])
y.append(ptos[rota[0]][1])      

ax.plot(x,y,'--k')
ax.plot(x,y,'ok',markersize=6)
ax.plot(x[0],y[0],'og',markersize=10)
ax.axis('off')


