# método de Euler
import matplotlib.pyplot as fig
import math
y=1
ysol=1
y_list=[y]
ysol_list=[ysol]
t=0
tf=5
n=50
h=tf/n
t_list=[t]
for i in range(0,n):
      t = t + h
      y = y + h*y
      ysol = 1*math.exp(t)
      t_list.append(t)
      y_list.append(y)
      ysol_list.append(ysol)
      
fig.plot(t_list,y_list,'-k', linewidth=5)
fig.plot(t_list,ysol_list,'--k', linewidth=5)
fig.grid()
fig.xlabel('tempo t', fontsize=16)
fig.ylabel('y(t)', fontsize=16)
fig.title('Solução para dy/dt = y', fontsize=16)
fig.legend(['Euler','Real'])

