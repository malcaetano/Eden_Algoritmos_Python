# conjunto de Mandelbrot
import numpy as np
import matplotlib.pyplot as fig
from numpy import newaxis
x=np.linspace(-2,1,5000)
y=np.linspace(-1.12,1.12,5000)
c=x[:,newaxis]+1j*y[newaxis,:]
z=0
for i in range(100):
    z=z**2+c
conj=(abs(z)<2)
fig.imshow(conj.T, extent=[-2,0.47,-1.12,1.12],cmap='nipy_spectral')
fig.axis('off')    

