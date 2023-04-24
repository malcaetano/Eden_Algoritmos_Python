############## EDO AQUECIMENTO GLOBAL #####################
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as fig

# ++++ parâmetros do modelo +++++
s=650            # capacidade de suporta da atmosfera
r=0.15           # taxa de emissao  
gamma=0.035      # taxa de crescimento do PIB        
alfa1=0.0006     # quantidade de remocao de CO2 pela floresta 
alfa2=0.00005    # relacao PIB com producao de CO2           
u1=0.00012       # investimento em reflorestamento          
u2=0.00008       # investimento em tecnologia limpa           
h=0.0001         # desmantamento das florestas

t0=0
tf=36
  
# condicoes inciais - emissao de CO2
Co20 = 398
# condicoes inciais - floresta (F)
F0 = 43
# condicoes inciais - PIB
Gdp0= 2787

# vetor do tempo de integracao
t = np.arange(0, tf, 0.1)

# Modelo Dinamico
def deriv(y, t, s,r,gamma,alfa1,alfa2,u1,u2,h):
    Co2, F, Gdp = y
    dCo2dt = r*Co2*(1-Co2/s)-alfa1*F+(alfa2-u2)*Gdp
    dFdt = u1*Gdp - h*F
    dGdpdt = gamma*Gdp
    return dCo2dt, dFdt, dGdpdt

# Condicao Inicial
y0 = Co20, F0, Gdp0

# Integrador numerico
ret = odeint(deriv, y0, t, args=(s,r,gamma,alfa1,alfa2,u1,u2,h))

Co2, F, Gdp = ret.T
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df=pd.read_excel('AqGlobal.xlsx',sheet_name='Planilha1')
df=df.set_index('ano')
figura, ax1 = fig.subplots(3,1)
ax1[0].plot(t+1961,Co2, '-k')
ax2=ax1[0].twinx()
df['co2'].plot(style='--o',color='black',ax=ax2)
ax1[0].set_xlabel('tempo',fontsize=10)
ax1[0].set_ylabel('CO2(milhões ton)', fontsize=10)
#fig.tight_layout()

ax1[1].plot(t+1961, F, '-k')
ax2=ax1[1].twinx()
df['floresta'].plot(style='--o',color='black',ax=ax2)
ax1[1].set_xlabel('tempo',fontsize=10)
ax1[1].set_ylabel('Floresta(milhões mm3)', fontsize=10)
#fig.tight_layout()

ax1[2].plot(t+1961, Gdp, '-k')
ax1[2].set_xlabel('tempo',fontsize=10)
ax1[2].set_ylabel('PIB(bilhões US$)', fontsize=10)
#fig.tight_layout()






