# Logistica
import matplotlib.pyplot as fig

r=3.84
a=0.1
x=[a]

for k in range(100):
        a = r*a*(1-a)
        x.append(a)  

fig.plot(x,'-k',linewidth=2)
fig.xlabel('Iteração', fontsize=16)
fig.ylabel('x[k]', fontsize=24)
fig.title('Logistica com r = 3.8', fontsize=16)

