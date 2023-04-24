# Otimizacao - Controle Otimo
#   min Integ {u**2}dt + (x(tf)-1)**2*tf + (v(tf - 0)**2*tf
#   suj a
#       dx/dt = v
#       dv/dt = u 
#-     x(0) = 0
#      v(0) = 0
#      x(tf) = 4
#      tf = 1
#      u - livre
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x = m.Var(value=0)  #### cond incial x(0) = 0
v = m.Var(value=0)  #### cond incial v(0) = 0
u = m.Var(fixed_initial=False) ### u - livre

p = np.zeros(nt)
p[-1]=1  # marca o ponto do tempo final
final = m.Param(value=p) # multiplica a cond. final da func Obj

####### Eq. diferenciais ########
m.Equation(x.dt()==v)
m.Equation(v.dt()==u)

####### restricoes #############
m.Equation((x-1)*final >= 0)
m.Equation(v*final <= 0)
m.Minimize(final*1e5*(x-1)**2)
m.Minimize(final*1e5*(v-0)**2)
###### Funcao Objetivo #########
m.Minimize(m.integral(u**2)*final)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=False) # solucao otima do problema

################# grafico da funcao 3D ################
fig.subplot(211)
fig.plot(m.time,x.value,'k-',label=r'$x$')
fig.plot(m.time,v.value,'k--',label=r'$v$')
fig.legend()
fig.grid()
fig.subplot(212)
fig.plot(m.time,u.value,'k-',label=r'$u$')
fig.legend()
fig.xlabel('Tempo')
fig.ylabel('Controle Ótimo')
fig.grid()



