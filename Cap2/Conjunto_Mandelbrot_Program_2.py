# conjunto de Mandelbrot 
import numpy as np
import matplotlib.pyplot as fig

def mandelbrot(ix,iy,iter):
    c=complex(ix,iy)
    z=0.0j
    for i in range(iter):
        z=z*z+c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return iter
    
col=5000
linha=5000
result=np.zeros([linha,col])

for lin_index, ix in enumerate(np.linspace(-2,1,num=linha)):
    for col_index, iy in enumerate(np.linspace(-1,1,num=col)):
      result[lin_index,col_index]=mandelbrot(ix,iy,100)

fig.figure(dpi=100)      
fig.imshow(result.T, cmap='magma', interpolation='bilinear',extent=[-2,1,-1,1])
fig.xlabel('Real')
fig.ylabel('Imaginário')
fig.show()

#### zoom em: ######
## x = [-1, 0.99]
## Im = [0.29, 0.3]
####################