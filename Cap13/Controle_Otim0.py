# Otimizacao - Controle Otimo
#   min Integ{u**2}dt
#   suj a
#       dx/dt = -2x + u
#-     x(0) = 10
#      x(1) = livre
#      tf = 1
#      u-livre
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x = m.Var(value=10)  #### cond incial x1(0) = 10
u = m.Var(fixed_initial=False) ### u - livre

p = np.zeros(nt)   # marca o ponto do tempo final
p[-1]=1
final = m.Param(value=p)

####### Eq. diferenciais ########
m.Equation(x.dt()== -2*x + u)
###### Funcao Objetivo #########
m.Minimize(m.integral(u**2)*final)

m.options.IMODE=6   # modo de otim dinamica e controle otimo
m.solve(disp=False) # solucao otima do problema

################# graficos ################
fig.subplot(211)
fig.plot(m.time,x.value,'k--',label=r'$x$')
fig.legend()
fig.grid()
fig.subplot(212)
fig.plot(m.time,u.value,'k-',label=r'$u$')
fig.legend()
fig.xlabel('Tempo')
fig.ylabel('Controle Ótimo')
fig.grid()



