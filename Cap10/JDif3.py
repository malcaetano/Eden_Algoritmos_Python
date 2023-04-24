# Jogos Diferenciais - PERSEGUIDOR X EVASOR
#### derivada em relacao a thetap #############
import numpy as np
import matplotlib.pyplot as fig
vp=1.1
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
stop_dist=0.03  # distancia entre o perseguidor e evasor
i=1
temp=0
delta=0.01 # incremento delta t

while  dist>=stop_dist:
    # ===== o evasor percebe que esta sendo perseguido e aumenta a veloc.
#     if dist<1 & ve==1
#         ve=ve*1.4;
#         stop_dist=0.05;
#     end
    temp=temp+delta 
    gama=np.arctan(yr/xr)
    thetae=np.arctan(np.tan(gama)+alpha*np.sqrt(1+np.tan(gama)**2));
    thetap=np.arctan((xr+ve*delta*np.cos(thetae))/(yr-ve*delta*np.sin(thetae)));
    xper=xper+delta*vp*np.cos(thetap)
    yper=yper-delta*vp*np.sin(thetap)
    xev=xev+delta*ve*np.cos(thetae)
    yev=yev-delta*ve*np.sin(thetae)
    xr=xev-xper;
    yr=yev-yper;
    dist=np.sqrt(xr**2+yr**2);
    xe.append(xev)
    ye.append(yev)
    xp.append(xper)
    yp.append(yper)
    fig.plot(xp,yp,'.b',xe,ye,'.k',markersize=5)
    fig.pause(0.2)

#for i in range(len(xp)):    
#    fig.plot(xp[i],yp[i],'.b',xe[i],ye[i],'.k',markersize=5)
#    fig.pause(0.2)
    


