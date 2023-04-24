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

nodes=[]
ptx=[]
pty=[]
for _ in range(20):
  x=random.uniform(-10,10)
  y=random.uniform(-10,10)
  ptx.append(x)
  pty.append(y)
  nodes.append((x,y))

def euclidean(a,b):
  return math.sqrt(pow(a[1]-b[1],2)+pow(a[0]-b[0],2)) 

world=pants.World(nodes,euclidean)

solver=pants.Solver(rho=0.5,q=1,t0=0.01,limit=50,ant_count=10)

solution=solver.solve(world)
print(solution.distance)
print(solution.tour)

solutions=solver.solutions(world)
best=float("inf")
for solution in solutions:
  assert solution.distance<best
  best=solution.distance
print(best)

########### figura ###############
rota=np.array(solution.tour)
xr=rota[:,0]
yr=rota[:,1]
ax=fig.subplot(111)
ax.plot(ptx,pty,'.k',markersize=15)
ax.plot(xr,yr,'-b')
ax.plot(xr[0],yr[0],'og',markersize=15)
ax.plot(xr[len(xr)-1],yr[len(yr)-1],'or',markersize=15)

fig.figure()
fig.plot(ptx,pty,'.k',markersize=15)
