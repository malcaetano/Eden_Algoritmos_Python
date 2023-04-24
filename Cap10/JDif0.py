# Jogos Diferenciais - PERSEGUIDOR X EVASOR Simples
import numpy as np
import matplotlib.pyplot as fig
vp=1.2
ve=1
alpha=vp/ve
xe=[]
xp=[]
ye=[]
yp=[]
xev=0.1  
yev=1
xper=0
yper=0
xr=xev-xper
yr=yev-yper
dist=np.sqrt(xr**2+yr**2); 
stop_dist=0.01  # distancia entre o perseguidor e evasor
i=1
temp=0
delta=0.01 # incremento delta t

while  dist>=stop_dist:
    thetae=np.arctan(yev+alpha*np.sqrt(xev**2+yev**2))/xev;
    xper=xper+delta*vp*xr/dist
    yper=yper+delta*vp*yr/dist
    xev=xev+delta*ve*np.cos(thetae);
    yev=yev+delta*ve*np.sin(thetae);
    xr=xev-xper;
    yr=yev-yper;
    dist=np.sqrt(xr**2+yr**2);
    xe.append(xev)
    ye.append(yev)
    xp.append(xper)
    yp.append(yper)

for i in range(0,len(xp),2):    
    fig.plot(xp[i],yp[i],'.k',xe[i],ye[i],'>k',markersize=5)
    fig.pause(0.1)
    


