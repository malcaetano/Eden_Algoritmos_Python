# Mapa Gingerbreadman
import matplotlib.pyplot as fig

x=[-0.3]
y=[0]
for i in range(10000):
    xn=1-y[i]+abs(x[i])
    yn=x[i]
    x.append(xn)
    y.append(yn)

fig.plot(x,y,'.k')
fig.xlabel('x')
fig.ylabel('y')

fig.figure()
fig.subplot(211)
fig.plot(x,'-k')
fig.xlabel('ITERAÇÕES',fontsize=16)
fig.ylabel('x',fontsize=16)
fig.subplot(212)
fig.plot(y,'-k')
fig.xlabel('ITERAÇÕES',fontsize=16)
fig.ylabel('y',fontsize=16)

