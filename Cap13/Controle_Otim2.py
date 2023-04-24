# Otimizacao - Controle Otimo
#   min Integ {u**2 + (u-x)**2 }dt + (x(tf)-4)*tf
#   suj a
#       dx/dt = x + u
#      dx2/dt = tf*(x-4)=0
#-     x(0) = 1
#      x(1) = 4
#      tf = 1
#      u - livre
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x = m.Var(value=1)  #### cond incial x(0) = 1
u = m.Var() ### u - livre

p = np.zeros(nt)
p[-1]=1  # marca o ponto do tempo final
final = m.Param(value=p) # multiplica a cond. final da func Obj

####### Eq. diferenciais ########
m.Equation(x.dt()==x+u)
m.Equation(final*(x-4)==0)

###### Funcao Objetivo #########
m.Minimize(m.integral(u**2+(u-x)**2)*final)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=False) # solucao otima do problema

################# grafico da funcao 3D ################
fig.subplot(211)
fig.plot(m.time,x.value,'k--',label=r'$x_1$')
fig.legend()
fig.grid()
fig.subplot(212)
fig.plot(m.time,u.value,'k-',label=r'$u$')
fig.legend()
fig.xlabel('Tempo')
fig.ylabel('Controle Ótimo')
fig.grid()



