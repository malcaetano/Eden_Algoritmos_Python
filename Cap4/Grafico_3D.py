import matplotlib.pyplot as fig
import numpy as ny
from mpl_toolkits import mplot3d

ax=fig.axes(projection='3d')

x=ny.linspace(-20,20,50)
y=ny.linspace(-20,20,50)
X, Y = ny.meshgrid(x,y)
Z=X**2+Y**2
ax.plot_surface(X,Y,Z, cmap='Greys')
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')
ax.set_zlabel('eixo Z')
