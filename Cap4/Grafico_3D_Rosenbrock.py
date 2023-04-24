import matplotlib.pyplot as fig
import numpy as ny
from mpl_toolkits import mplot3d

ax=fig.axes(projection='3d')

x=ny.linspace(-2,2,50)
y=ny.linspace(-1,3,50)
X, Y = ny.meshgrid(x,y)
Z = (1-X)**2 + 100*(Y-X**2)**2
ax.contour3D(X,Y,Z, 100)
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')
ax.set_zlabel('eixo Z')
