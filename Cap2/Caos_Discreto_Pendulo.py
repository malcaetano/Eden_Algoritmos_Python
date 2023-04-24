# Pendulo com atrito
import matplotlib.pyplot as fig
import math as mt
############## lista vazia para angulo e freq
omega=[]
theta=[]
############# condição inicial das variáveis
x=0
y=mt.pi/2
############ quantidade de simulações
n=10000
########### valores dos parâmetros
dt=0.01
Om=3/2
q=3/4
f=0
#######################################################
#    Equacões da Dinâmica
######################################################
w=x
th=y
t=0
for j in range(n):
        t=t+dt
        w=w-dt*(Om**2*mt.sin(th)+q*w-f*mt.sin(t))
        th=th+dt*w
        omega.append(w)
        theta.append(th)

################ Gráficos ###########################
fig.plot(theta,omega,'-k')
fig.xlabel('theta')
fig.ylabel('omega')

fig.figure()
fig.subplot(211)
fig.plot(omega,'-k')
fig.xlabel('ITERAÇÕES',fontsize=16)
fig.ylabel('omega',fontsize=16)
fig.subplot(212)
fig.plot(theta,'-k')
fig.xlabel('ITERAÇÕES',fontsize=16)
fig.ylabel('theta',fontsize=16)

