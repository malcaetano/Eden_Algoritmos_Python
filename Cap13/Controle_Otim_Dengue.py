# Otimizacao - Controle Otimo da Dengue
#   min tf
#   suj a
#   dx1/dt=((alpha_r*(1-mu*m.sin(omega*t))-alpha_m-x4)*x1-u1)*tf)
#   dx2/dt= ((alpha_r*(1-mu*m.sin(omega*t))-alpha_m-x4)*x2+beta*(x1-x2)*x3-u1)*tf)
#   dx3/dt= (-x3+rho*x2)*(P-x3)*tf)
#   dx4/dt=  (-tau*x4+theta*x3+u2)*tf)
#      tf = livre
#      0 <= u <= 6
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x1 = m.Var(value=1)      #### cond incial x1(0) = 1
x2 = m.Var(value=0.12)   #### cond incial x2(0) = 0.12
x3 = m.Var(value=0.004)  #### cond incial x3(0) = 0.004
x4 = m.Var(value=0.05)   #### cond incial x4(0) = 0.05
t = m.Var()
alpha_r = 0.20
alpha_m = 0.18
beta = 0.30
lambd = 0.15
rho = 0.10
theta = 0.005
tau = 0.1
eta = 1
P = 1
phi = 0
mu = 0.08
gama_d = 1
gama_e = 0.8
gama_f = 0.4
omega = np.pi*2/52

##### controle variavel dentro dos limites ########
u1 = m.MV(value = 0, lb = 0, ub = 1) ### 0<=u<=1
u1.STATUS = 1 # valor variavel do passo 1 ate o 
#            # final em todos os passos de integracao

u2 = m.MV(value = 0, lb = 0, ub = 1) ### 0<=u<=1
u2.STATUS = 1 # valor variavel do passo 1 ate o 
#            # final em todos os passos de integracao
#####################################################

p = np.zeros(nt)
p[-1]=1  # marca o ponto do tempo final
final = m.Param(value=p) # multiplica a cond. final da func Obj

# Tempo final livre
##################################
tf=m.FV(value=1, lb=0.1, ub=5.0) # --- tempo final livre
tf.STATUS=1 # valor variavel do passo 1 ate o final

####### Eq. diferenciais parametrizadas pelo tf ########
m.Equation(x1.dt() == ((alpha_r*(1-mu*m.sin(omega*t+phi))-alpha_m-x4)*x1-u1)*tf)
m.Equation(x2.dt() == ((alpha_r*(1-mu*m.sin(omega*t+phi))-alpha_m-x4)*x2+beta*(x1-x2)*x3-u1)*tf)
m.Equation(x3.dt() == (-eta*x3+rho*x2)*(P-x3)*tf)
m.Equation(x4.dt() == (-tau*x4+theta*x3+u2)*tf)
m.Minimize(final*1e5*(x1-0)**2)
m.Minimize(final*1e5*(x2-0)**2)
m.Minimize(final*1e5*(x3-0)**2)

m.Equation(x1>0)
m.Equation(x2>0)
m.Equation(x3>0)
m.Equation(x4>0)

###### Funcao Objetivo - Minimo Controle #########
m.Obj(gama_d*x3**2+gama_f*u1**2+gama_e*u2**2)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=True) # solucao otima do problema

print(' ')
print('#### tempo final  #####')
print(' ')
print('tempo final (semanas) = ' + str(tf.value[0]*52/(np.pi*2)))
print(' ')
print('##############################')
################# graficos ################

figura, ax = fig.subplots()

tempo_real=m.time*tf.value[0]*52/(np.pi*2)

ax.plot(tempo_real,x1.value,'k-o',label=r'$x1$')
ax.set_ylabel('densidade de mosquitos (x1)', fontsize=16)
ax.yaxis.tick_left()
fig.xticks(tempo_real[::10],rotation=30)
ax.text(13,0.5,s='x1',fontsize=16)
fig.title('Otmização no Combate a Dengue', fontsize=20)
fig.xlabel('SEMANAS', fontsize=18)

ax_1=ax.twinx()
ax_1.spines['right'].set_position(('axes', 0.03))
ax_1.plot(tempo_real,x2.value,'k--',label=r'$x2$')
ax_1.text(13,0.03,s='x2',fontsize=16)
ax_1.yaxis.set_label_position("left")
ax_1.yaxis.set_label_coords(0.02,0.5)
ax_1.set_ylabel('densidade de mosquitos infectados (x2)', fontsize=16)

ax2=ax.twinx()
ax2.spines['left'].set_position(('axes', 1.0))

ax2.plot(tempo_real,x3.value,'k-.',label=r'$x3$')
ax2.yaxis.set_label_position("left")
ax2.text(13,0.0075,s='x3',fontsize=16)
ax2.set_ylabel('número de pessoas com dengue (x3)', fontsize=16)


ax3=ax.twinx()
ax3.spines['left'].set_position(('axes', 0.97))

ax3.plot(tempo_real,x4.value,'k-',label=r'$x4$')
ax3.yaxis.tick_left()
ax3.yaxis.set_label_position("left")
ax3.set_ylabel('nível de motivação popular (x4)', fontsize=16)
ax3.text(30,1,s='x4',fontsize=16)

ax2.spines["right"].set_edgecolor('black')

fig.figure()
fig.subplot(211)
fig.plot(tempo_real,u1.value,'k-',label=r'$u$')
fig.xticks(tempo_real[::10],rotation=30)
fig.xlabel('SEMANAS', fontsize=18)
fig.ylabel('Investimento em Inseticida',fontsize=15)
fig.grid()
fig.title('Controle Ótimo da Dengue',fontsize=20)

fig.subplot(212)
fig.plot(tempo_real,u2.value,'k-',label=r'$u$')
fig.xticks(tempo_real[::10],rotation=30)
fig.xlabel('SEMANAS', fontsize=18)
fig.ylabel('Investimento em Campanha Educacional',fontsize=15)
fig.grid()


