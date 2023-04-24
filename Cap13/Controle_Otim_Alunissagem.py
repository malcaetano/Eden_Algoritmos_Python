# Otimizacao - Controle Otimo
#   min tf
#   suj a
#       dx/dt = v
#       dv/dt = u - 1 
#-     x(0) = 10
#      v(0) = 0
#      x(tf) = 0
#      v(tf) = 0
#      tf = livre
#      0 <= u <= 2
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x = m.Var(value=10)  #### cond incial x(0) = 0
v = m.Var(value=0)  #### cond incial v(0) = 0

##### controle variavel dentro dos limites ########
u = m.MV(value = 0, lb = 0, ub = 2) ### 0<=u<=2
u.STATUS = 1 # valor variavel do passo 1 ate o 
#            # final em todos os passos de integracao

#####################################################
p = np.zeros(nt)
p[-1]=1  # marca o ponto do tempo final
final = m.Param(value=p) # multiplica a cond. final da func Obj

# Tempo final livre
##################################
tf=m.FV(value=1.0, lb=0.1, ub=100.0) # --- tempo final livre
tf.STATUS=1 # valor variavel do passo 1 ate o final

####### Eq. diferenciais parametrizadas pelo tf ########
m.Equation(x.dt() == v*tf)
m.Equation(v.dt() == (u - 1)*tf)

####### restricoes #############
m.Equation(x*final == 0)
m.Equation(v*final == 0)

###### Funcao Objetivo - Min tempo final tf#########
m.Obj(tf)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=False) # solucao otima do problema

print(' ')
print('#### tempo final mínimo #####')
print('tempo final = ' + str(tf.value[0]))
print('##############################')
################# graficos ################
fig.subplot(211)
tempo_real=m.time*tf.value[0]
fig.plot(tempo_real,x.value,'k-',label=r'$x$')
fig.plot(tempo_real,v.value,'k--',label=r'$v$')
fig.legend(fontsize=14)
fig.grid()
fig.subplot(212)
fig.plot(tempo_real,u.value,'k-',label=r'$u$')
fig.legend(fontsize=14)
fig.xlabel('Tempo')
fig.ylabel('Controle Ótimo')
fig.grid()



