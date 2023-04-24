#########################################################
#    precisa instalar essas duas bibliotecas
#    pip install geopy
#    conda install -c anaconda basemap
########################################################
import pandas as pd
import numpy as np
import pants
import math
import os

os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr

from mpl_toolkits.basemap import Basemap
map = Basemap(width=9000000,height=8000000,projection='lcc',
            resolution=None,lat_1=-20.,lat_2=-20,lat_0=-15,lon_0=-40.)

map.drawparallels(np.arange(-90.,120.,30.),color='black')
map.drawmeridians(np.arange(0.,420.,60.),color='black')
map.shadedrelief()

df=pd.read_excel('Cidades.xlsx',sheet_name='Planilha1')
df.index=range(len(df.index))

x=np.zeros(len(df))
y=np.zeros(len(df))
for i in range(len(df)):
         test_str = df['coord'][i]
         res = eval(test_str) 
         x[i]=res[0]
         y[i]=res[1]
         long, lat = map(*zip(*[res]))
         map.plot(long, lat, marker='o', markersize=5, 
                  markerfacecolor='black',markeredgecolor='k')

nodes=[]
ptx=[]
pty=[]
for i in range(len(df)):
  ptx.append(x[i])
  pty.append(y[i])
  nodes.append((x[i],y[i]))

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

for i in range(1,len(rota)):
        map.drawgreatcircle(xr[i-1],yr[i-1],xr[i],yr[i],linewidth=2,color='k')

map.drawgreatcircle(xr[0],yr[0],xr[0],yr[0],marker='o',
                    markersize=10,color='g',markeredgecolor='k')






