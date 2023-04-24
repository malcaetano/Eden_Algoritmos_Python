# Jogos Diferenciais - PERSEGUIDOR X EVASOR
import numpy as np
import matplotlib.pyplot as fig
vp=2
ve=1
alpha=vp/ve
xe=[]
xp=[]
ye=[]
yp=[]
xev=0.6  
yev=1
xper=0
yper=0
xr=xev-xper
yr=yev-yper
dist=np.sqrt(xr**2+yr**2); 
stop_dist=0.01  # distancia entre o perseguidor e evasor
i=1
temp=0
delta=0.02 # incremento delta t

while  dist>=stop_dist:
    # ===== o evasor percebe que esta sendo perseguido e aumenta a veloc.
    if dist<1 and ve==1:
         ve=ve*1.9
         stop_dist=0.05
    temp=temp+delta 
    gama=np.arctan(yr/xr)
    thetae=np.arctan(np.tan(gama)+alpha*np.sqrt(1+np.tan(gama)**2));
    thetap=np.arctan(np.tan(gama)+np.sqrt(1+np.tan(gama)**2)/alpha);
    xper=xper+delta*vp*np.cos(thetap)+delta*xr*alpha**2/(alpha**2-1);
    yper=yper+delta*vp*np.sin(thetap)+delta*(alpha**2*yr+
                             alpha*np.sqrt(yr**2+xr**2))/(alpha**2-1);
    xev=xev+delta*ve*np.cos(thetae);
    yev=yev+delta*ve*np.sin(thetae);
    xr=xev-xper;
    yr=yev-yper;
    dist=np.sqrt(xr**2+yr**2);
    xe.append(xev)
    ye.append(yev)
    xp.append(xper)
    yp.append(yper)
    fig.plot(xp,yp,'ok',xe,ye,'>k',markersize=5)
    fig.pause(0.2)

    


