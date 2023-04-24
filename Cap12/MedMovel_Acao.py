#################################################################
#                                                               #
#   ANTES DE RODAR A PRIMEIRA VEZ PRECISA INSTALAR A BIBLIOTECA #
#    pip install yahoo-fin                              #
#                                                               #
#################################################################

import matplotlib.pyplot as fig
import datetime as dt
from yahoo_fin.stock_info import *

################ importar a acao ############################
inicio=dt.datetime(2021,6,1)
fim=dt.datetime(2022,8,26)
df = get_data('PETR4.SA', start_date=inicio, end_date=fim)

df['close'].plot(color='k',lw=2,alpha=0.6)
df['med_mov']=df['close'].rolling(window=30,min_periods=0).mean()
df['med_mov'].plot(color='k',lw=3,style='--')

fig.grid()
fig.title('Petrobras(PETR4) (2021-2022)',fontsize=18,weight='bold')
fig.legend(['PETR4','Média Móvel 30 dias'])




