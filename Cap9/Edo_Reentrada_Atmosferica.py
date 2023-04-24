############## EDO Reentrada Atmosferica #####################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
from math import sin, cos, tan, exp, radians, degrees
from mpl_toolkits import mplot3d
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap

# ++++ parâmetros do modelo +++++
mit=3.98600440e+5       # GM de TERRA km3/seg2
ro0=1.217e9             # densidade ao nivel do mar
beta=0.149              # parametro de ajuste do modelo de densidade atm
S=(18.73)*10**(-6)      # area da superficie de referencia do veiculo
cd0=1.174               # coeficiente de arrasto
cd1=0.9                 # coeficiente de arrasto
cl=0.6                  # coeficiente de sustentacao
m=4536                  # massa do veiculo em kg 
g=0.00979827621756667   # forca gravitacional em km/s2
r_Terra = 6378.140      # raio medio da Terra [km]

t0=0
dia=86400   # quantidade de segundos em um dia
tf=0.02*dia
  
# condicoes inciais - posicao altitude (h)
h0 = 122
# condicoes inciais - longitude (theta)
theta0 = radians(-80)
# condicoes inciais - Latitude (phi)
phi0= radians(-25)
# condicoes inciais - velocidade  (v)
v0 = 7.6
# condicoes inciais - angulo de trajetoria (gamma)
gamma0 = radians(-4)
# condicoes inciais - psi
psi0= radians(30)
# condicoes iniciais da distancia percorrida (range x)
x0=0
# vetor do tempo de integracao
t = np.arange(0, tf, 0.1)

# Modelo Dinamico
def deriv(y, t, S,ro0,beta,r_Terra,cd0,cd1,cl,m):
    h, theta,phi,v,gamma,psi,x = y
    ro = ro0*exp(-beta*h)
    u=radians(55)
    cd=cd0-cd1*cos(u)
    dhdt = v*sin(gamma)
    dthetadt = v*cos(gamma)*cos(psi)/((r_Terra+h)*cos(phi))
    dphidt = v*cos(gamma)*sin(psi)/(r_Terra+h)
    dvdt = -0.5*S*ro*v**2*cd/m-g*sin(gamma)
    dgammadt = 0.5*S*ro*v*cl/m-(g/v-v/(r_Terra+h))*cos(gamma)
    dpsidt = -(v/(r_Terra+h))*cos(gamma)*cos(psi)*tan(phi)
    dxdt=v*cos(gamma)
    return dhdt,dthetadt,dphidt,dvdt,dgammadt,dpsidt,dxdt 

# Condicao Inicial
y0 = h0, theta0, phi0, v0, gamma0, psi0, x0

# Integrador numerico
ret = odeint(deriv, y0, t, args=(S,ro0,beta,r_Terra,cd0,cd1,cl,m))
h, theta, phi, v, gamma, psi, x = ret.T
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fig.subplot(221)
fig.plot(x, h, '-k')
fig.xlabel('distância',fontsize=10)
fig.ylabel('altitude h (km)', fontsize=10)
fig.tight_layout()
fig.subplot(222)
fig.plot(t, v, '--k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('velocidade v (km/s)', fontsize=10)
fig.tight_layout()
fig.subplot(223)
fig.plot(t, np.degrees(gamma), '--k')
fig.xlabel('tempo',fontsize=10)
fig.ylabel('ângulo(gamma) graus', fontsize=10)
fig.tight_layout()
fig.subplot(224)
fig.plot(np.degrees(theta), np.degrees(phi), ':k')
fig.xlabel('longitude (theta) graus',fontsize=10)
fig.ylabel('latitude (phi) graus', fontsize=10)
fig.tight_layout()

fig.figure()
ax=fig.axes(projection='3d')
ax.plot3D(np.degrees(theta),np.degrees(phi),h, color='black')
ax.set_xlabel('longitude (theta) graus')
ax.set_ylabel('latitude (phi) graus') 
ax.set_zlabel('altitude h (km)')


latd = np.degrees(phi)
long = np.degrees(theta)


fig.figure()
map = Basemap(projection='ortho', lat_0=0, lon_0=-80,
              resolution='l', area_thresh=1000.0)
lon, lat=map(long,latd) 
map.drawcoastlines()
map.drawcountries() 
map.drawmapboundary()

map.plot(lon, lat, marker='o', markersize=6, linewidth=0)
fig.show()

fig.figure()
map = Basemap(projection='mill',lon_0=0)
# plot linhas da costa,valores dos meridianos e dos paralelos
map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
lon, lat=map(long,latd)
map.plot(lon, lat, marker='o', markersize=6, linewidth=0)
fig.show()


