# Otimizacao - Controle Otimo na Emissao do CO2
#   min tf
#   suj a
#    dx/dt = (alpha_0*x*(1-x/s)-alpha_1*z+(alpha_2-u2)*y)*tf)
#    dy/dt = (gama*y)*tf)
#    dx/dt = (u1*y-h*z)*tf)
#      tf = livre
#      0 <= u1 <= 750
#      0 <= u2 <= 420
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x = m.Var(value=450)      #### cond incial x(0) = 450(ton/ano)
y = m.Var(value=433.16)   #### cond incial y(0) = 433.16(1E6 US$)
z = m.Var(value=3649)     #### cond incial z(0) = 3649 km2

alpha_0 = 1.2
alpha_1 = 0.1
alpha_2 = 0.0003
s = 1900
h = 0.1
gama = 0.05
q = 1
r1 = 2.3e+6
r2 = 8e+6
Peso = 1e5


##### controle variavel dentro dos limites ########
u1 = m.MV(value = 0, lb = 0, ub = 750) ### 0<=u<=750
u1.STATUS = 1 # valor variavel do passo 1 ate o 
#            # final em todos os passos de integracao

u2 = m.MV(value = 0, lb = 0, ub = 420) ### 0<=u<=420
u2.STATUS = 1 # valor variavel do passo 1 ate o 
#            # final em todos os passos de integracao
#####################################################

p = np.zeros(nt)
p[-1]=1  # marca o ponto do tempo final
final = m.Param(value=p) # multiplica a cond. final da func Obj

# Tempo final livre
##################################
tf=m.FV(value=1, lb=0.1, ub=10.0) # --- tempo final livre
tf.STATUS=1 # valor variavel do passo 1 ate o final

####### Eq. diferenciais parametrizadas pelo tf ########
m.Equation(x.dt() == (alpha_0*x*(1-x/s)-alpha_1*z+(alpha_2-u2)*y)*tf)
m.Equation(y.dt() == (gama*y)*tf)
m.Equation(z.dt() == (u1*y-h*z)*tf)
m.Minimize(final*Peso*(x-50)**2)
m.Minimize(final*Peso*(z-3500)**2)

m.Equation(x>0)
m.Equation(y>0)
m.Equation(z>0)

###### Funcao Objetivo - Minimo Controle #########
m.Obj(q*x**2+r1*u1**2+r2*u2**2)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=True) # solucao otima do problema

print(' ')
print('#### tempo final  #####')
print(' ')
print('tempo final (anos) = ' + str(tf.value[0]))
print(' ')
print('##############################')
################# graficos ################

figura, ax = fig.subplots()

tempo_real=m.time*tf.value[0]

ax.plot(tempo_real,x.value,'k-o',label=r'$x$')
ax.set_ylabel('Milhões ton Co2 liberado na Atm (x)', fontsize=16)
ax.yaxis.tick_left()
fig.xticks(tempo_real[::10],rotation=30)
ax.text(4,300,s='x',fontsize=16)
fig.title('Otimização na Emissão de CO2', fontsize=20)
fig.xlabel('ANOS', fontsize=18)

ax_1=ax.twinx()
ax_1.spines['right'].set_position(('axes', 0.03))
ax_1.plot(tempo_real,y.value,'k--',label=r'$y$')
ax_1.text(4,520,s='y',fontsize=16)
ax_1.yaxis.set_label_position("left")
ax_1.yaxis.set_label_coords(0.02,0.5)
ax_1.set_ylabel('PIB - milhares de US$ (y)', fontsize=16)

ax2=ax.twinx()
ax2.spines['left'].set_position(('axes', 1.0))

ax2.plot(tempo_real,z.value,'k-',label=r'$z$')
ax2.yaxis.set_label_position("left")
ax2.text(6,2900,s='z',fontsize=16)
ax2.set_ylabel('área de floresta - km2 x 1E3 (z)', fontsize=16)


fig.figure()
fig.subplot(211)
fig.plot(tempo_real,u1.value,'k-',label=r'$u$')
fig.xticks(tempo_real[::10],rotation=30)
fig.xlabel('ANOS', fontsize=18)
fig.ylabel('Reflorestamento(u1) - milhões US$',fontsize=15)
fig.grid()
fig.title('Controle Ótimo na Emissão de CO2',fontsize=20)

fig.subplot(212)
fig.plot(tempo_real,u2.value,'k-',label=r'$u$')
fig.xticks(tempo_real[::10],rotation=30)
fig.xlabel('ANOS', fontsize=18)
fig.ylabel('Tecnologia Limpa(u2) - milhões US$',fontsize=15)
fig.grid()


