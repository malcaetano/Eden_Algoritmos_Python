import matplotlib.pyplot as fig
import numpy as np
from mpl_toolkits import mplot3d

ax=fig.axes(projection='3d')

x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
X, Y = np.meshgrid(x,y)
Z=1.5*np.exp(1/(1+(X-1)**2+(Y-1)**2))-2.5*np.exp(1/(1+\
                 (1/4)*(X+0.5)**2+(1/36)*(Y-1)**2))+\
                 2*np.exp(1/(1+(X-2)**2+(Y-2)**2))+\
                 2*np.exp(1/(1+(X-1)**2+(Y+1)**2))
ax.plot_surface(X,Y,Z, cmap='gray')
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')
ax.set_zlabel('eixo Z')

xopt1=[2.0143,1.81,1.92,2.13,1.90]
yopt1=[1.95056,2.02,2.03,1.92,1.77]
zopt1=[6.0574,5.805,5.96,5.97,5.88]
ax.scatter3D(xopt1,yopt1,zopt1,color='red',marker='*',s=100)