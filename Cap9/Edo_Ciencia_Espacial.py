############## EDO Ciencia Espacial #####################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
import math as m
from mpl_toolkits import mplot3d
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap

# ++++ parâmetros do modelo +++++
au=1.495978707e+8 # unidade astronomica em Km
mit=3.98600440e+5 # GM de TERRA km3/seg2
milua=4.9028e+3 # GM da Lua km3/seg2
t0=0
dia=86400   # quantidade de segundos em um dia
tf=0.1*dia
  
# condicoes inciais - posicao X
xL0 = -806.991791465944
# condicoes inciais - posicao Y
yL0 = -5505.916560978470
# condicoes inciais - posicao Z
zL0= -3902.703452279670

# condicoes inciais - velocidade dX
dxL0 = 6.14791445996455
# condicoes inciais - velocidade dY
dyL0 = 2.00114921418649
# condicoes inciais - velocidade dZ
dzL0= -4.10247590688757

# vetor do tempo de integracao
t = np.arange(0, tf, 0.8)

# Modelo Dinamico
def deriv(y, t, milua):
    xL,yL,zL,dxL,dyL,dzL = y
    r=m.sqrt(xL**2+yL**2+zL**2)
    dx1dt = dxL
    dx2dt = dyL
    dx3dt = dzL
    dx4dt = -mit*xL/r**3
    dx5dt = -mit*yL/r**3
    dx6dt = -mit*zL/r**3
    return dx1dt, dx2dt, dx3dt, dx4dt, dx5dt, dx6dt

# Condicao Inicial
y0 = xL0, yL0, zL0, dxL0, dyL0, dzL0

# Integrador numerico
ret = odeint(deriv, y0, t, args=(milua,))
X, Y, Z, dX, dY, dZ = ret.T
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fig.subplot(221)
fig.plot(t, X, '-k')
fig.xlabel('tempo',fontsize=16)
fig.ylabel('X', fontsize=16)
fig.tight_layout()
fig.subplot(222)
fig.plot(t, Y, '--k')
fig.xlabel('tempo',fontsize=16)
fig.ylabel('Y', fontsize=16)
fig.tight_layout()
fig.subplot(223)
fig.plot(t, Y, '--k')
fig.xlabel('tempo',fontsize=16)
fig.ylabel('Z', fontsize=16)
fig.tight_layout()
fig.subplot(224)
fig.plot(X, Y, ':k')
fig.xlabel('X',fontsize=16)
fig.ylabel('Y', fontsize=16)
fig.tight_layout()

fig.figure()
ax=fig.axes(projection='3d')
ax.plot3D(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig.figure()
# Criando a Terra como uma esfera no gráfico
N = 50
phi = np.linspace(0, 2 * np.pi, N)
theta = np.linspace(0, np.pi, N)
theta, phi = np.meshgrid(theta, phi)

r_Terra = 6378.14  # raio medio da Terra [km]
X_Terra = r_Terra * np.cos(phi) * np.sin(theta)
Y_Terra = r_Terra * np.sin(phi) * np.sin(theta)
Z_Terra = r_Terra * np.cos(theta)

# Gráfico da Terra e Órbita
ax = fig.axes(projection='3d')
ax.scatter3D(X_Terra, Y_Terra, Z_Terra, marker='.',color='gray', alpha=0.3)
ax.plot3D(X, Y, Z, 'red')
ax.view_init(25, 34)  # angulo inicial da visualizacao
fig.title('Órbita do Veículo Espacial')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_zlabel('Z [km]')

xyzlim = np.array([ax.get_xlim3d(), ax.get_ylim3d(),      
                   ax.get_zlim3d()]).T
XYZlim = np.asarray([min(xyzlim[0]), max(xyzlim[1])])
ax.set_xlim3d(XYZlim)
ax.set_ylim3d(XYZlim)
ax.set_zlim3d(XYZlim * 3/4)
fig.show()

latd = np.degrees(np.arcsin(Z/r_Terra))
long = np.degrees(np.arctan2(Y, X))


fig.figure()
map = Basemap(projection='ortho', lat_0=-20, lon_0=-10,
              resolution='l', area_thresh=1000.0)
lon, lat=map(long,latd) 
map.drawcoastlines()
map.drawcountries() 
map.drawmapboundary()

map.plot(lon, lat, marker='o', markersize=6, linewidth=0)
fig.show()

fig.figure()
map = Basemap(projection='mill',lon_0=0)
# plot coastlines, draw label meridians and parallels.
map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
lon, lat=map(long,latd)
map.plot(lon, lat, marker='o', markersize=6, linewidth=0)
fig.show()