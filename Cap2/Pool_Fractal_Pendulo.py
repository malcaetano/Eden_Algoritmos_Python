import multiprocessing as mp
import numpy as np
import math as mt
import matplotlib.pyplot as fig
from time import time
from scipy.integrate import odeint

def deriv(s, t):
    X, Y = s
    dXdt = Y
    dYdt = -0.02*Y - 1*X*(X**2) + 7*mt.cos(t*1)
    return dXdt, dYdt

def EDO(t):
    eix=[]
    eiy=[]
    X0=1
    Y0=0
    s0 = X0, Y0
        # Integracao do sistema #########################
    res = odeint(deriv, s0, t)
    X, Y = res.T
    eix.append(X)
    eiy.append(Y)
    return eix,eiy
 
if __name__ == '__main__':
          t0=time()
          p=mp.Pool(processes=1)
          t = np.linspace(0, 10000*(2*np.pi), 100000000)
          res=p.map(EDO,(t,))
          p.close()
          print(time()-t0)
          res=np.array(res)
          x=[res[0,0][0][10000*i-10:10000*i] for i in range(1,10000)]
          y=[res[0,1][0][10000*i-10:10000*i] for i in range(1,10000)]
          fig.scatter(x,y,color='black',s=4)
          fig.xlabel('POSIÇÃO', fontsize=16)
          fig.ylabel('VELOCIDADE', fontsize=16)
          
