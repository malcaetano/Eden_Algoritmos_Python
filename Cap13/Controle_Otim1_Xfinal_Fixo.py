# Otimizacao - Controle Otimo
#   min int{0.5*x1**2}
#   suj a
#       dx1/dt = u
#-     x1(0) = 1
#      x1(tf) = 0.5
#      tf = 2
#      -1 <= u <= 1
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,2,nt)
x1 = m.Var(value=1)  #### cond incial x1(0) = 1
u = m.Var(value = 0, lb = -1, ub = 1) ### -1<=u<=1

p = np.zeros(nt)
p[-1]=1
final = m.Param(value=p)

####### Eq. diferenciais ########
m.Equation(x1.dt()==u)
m.Equation(final*(x1-0.5)==0)

###### Funcao Objetivo #########
m.Minimize(m.integral(0.5*x1**2)*final)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=False) # solucao otima do problema

print(' ')
print('########### Valor Função Obejtivo Otimizada ############')
print('J = : ' + str(m.options.OBJFCNVAL))
print('#######################################################')
      
################# graficos ################
fig.subplot(211)
fig.plot(m.time,x1.value,'k--',label=r'$x_1$')
fig.legend()
fig.grid()
fig.subplot(212)
fig.plot(m.time,u.value,'k-',label=r'$u$')
fig.legend()
fig.xlabel('Tempo')
fig.ylabel('Controle Ótimo')
fig.grid()





