# Otimizacao - Controle Otimo
#   min tf
#   suj a
#      dx1/dt = x2*tf
#      dx2/dt = (x3**2/x1-1/x1**2+T*m.sin(u))*tf
#      dx3/dt = (-x2*x3/x1+T*m.cos(u))*tf
#      dx4/dt = (x3/x1)
#      tf = livre
#      0 <= u <= 6
##############################################
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as fig

m = GEKKO()
nt=101
m.time = np.linspace(0,1,nt)
x1 = m.Var(value=1)  #### cond incial x1(0) = 1
x2 = m.Var(value=0)  #### cond incial x2(0) = 0
x3 = m.Var(value=1)  #### cond incial x3(0) = 1
x4 = m.Var(value=0)  #### cond incial x4(0) = 0

T = 0.1405   # forca de empuzo adimensional

##### controle variavel dentro dos limites ########
u = m.MV(value = 0, lb = 0, ub = 6) ### 0<=u<=6
u.STATUS = 1 # valor variavel do passo 1 ate o 
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
m.Equation(x1.dt() == x2*tf)
m.Equation(x2.dt() == (x3**2/x1-1/x1**2+T*m.sin(u))*tf)
m.Equation(x3.dt() == (-x2*x3/x1+T*m.cos(u))*tf)
m.Equation(x4.dt() == (x3/x1)*tf)
m.Minimize(final*1e5*(x1-1.52558)**2)
m.Minimize(final*1e5*(x2-0.0)**2)
m.Minimize(final*1e5*(x3-0.8098)**2)


###### Funcao Objetivo - Minimo Controle #########
m.Obj(u**2)
m.options.IMODE=6   # mode de otim dinamica e controle
m.solve(disp=True) # solucao otima do problema

print(' ')
print('#### tempo final mínimo #####')
print(' ')
print('tempo final (dias) = ' + str(tf.value[0]*365.25/(2*np.pi)))
print(' ')
print('##############################')
################# graficos ################

figura, ax = fig.subplots()

tempo_real=m.time*tf.value[0]*365.25/(2*np.pi)

ax.plot(tempo_real,x1.value,'k-o',label=r'$x1$')
ax.set_ylabel('distância Terra-Marte (x1)', fontsize=16)
ax.yaxis.tick_left()
fig.xticks(tempo_real[::10],rotation=30)
ax.text(45,1.02,s='x1',fontsize=16)
fig.title('Otmização Trajetória Terra-Marte', fontsize=20)
fig.xlabel('DIAS', fontsize=18)

ax_1=ax.twinx()
ax_1.spines['right'].set_position(('axes', 0.03))
ax_1.plot(tempo_real,x2.value,'k--',label=r'$x2$')
ax_1.text(60,0.15,s='x2',fontsize=16)
ax_1.yaxis.set_label_position("left")
ax_1.yaxis.set_label_coords(0.02,0.5)
ax_1.set_ylabel('velocidade radial (x2)', fontsize=16)

ax2=ax.twinx()
ax2.spines['left'].set_position(('axes', 1.0))

ax2.plot(tempo_real,x3.value,'k-.',label=r'$x3$')
ax2.yaxis.set_label_position("left")
ax2.text(160,0.7,s='x3',fontsize=16)
ax2.set_ylabel('velocidade circular (x3)', fontsize=16)


ax3=ax.twinx()
ax3.spines['left'].set_position(('axes', 0.97))

ax3.plot(tempo_real,x4.value,'k-',label=r'$x4$')
ax3.yaxis.tick_left()
ax3.yaxis.set_label_position("left")
ax3.set_ylabel('ângulo de fase (x4)', fontsize=16)
ax3.text(182,2.4,s='x4',fontsize=16)

ax2.spines["right"].set_edgecolor('black')

fig.figure()
ang_graus= np.array(u.value)*180/np.pi
fig.plot(tempo_real,ang_graus,'k-',label=r'$u$')
fig.xticks(tempo_real[::10],rotation=30)
fig.xlabel('DIAS', fontsize=18)
fig.ylabel('Controle Ótimo (ângulo de empuxo em graus)',fontsize=16)
fig.grid()

x_vet=x1.value*np.cos(x4.value)
y_vet=x1.value*np.sin(x4.value)
theta=np.arange(0,np.pi*2.1,0.1)
x_terra=np.cos(theta)
y_terra=np.sin(theta)
x_marte=1.52558*np.cos(theta)
y_marte=1.52558*np.sin(theta)

fig.figure()
fig.plot(x_terra,y_terra,'k--',x_marte,y_marte,'k--')
fig.plot(x_vet,y_vet,'k-',linewidth=5)
fig.xlabel('X-distância',fontsize=18)
fig.ylabel('Y-distância',fontsize=18)
fig.title('TRAJETÓRIA ÓTIMA TERRA-MARTE', fontsize = 20)




