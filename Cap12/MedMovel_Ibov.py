#################################################################
#                                                               #
#   ANTES DE RODAR A PRIMEIRA VEZ PRECISA INSTALAR A BIBLIOTECA #
#    pip install pandas_datareader                              #
#                                                               #
#################################################################

import matplotlib.pyplot as fig
import datetime as dt
from yahoo_fin.stock_info import *

################ importar a acao ############################
inicio=dt.datetime(2000,1,1)
fim=dt.datetime(2022,8,26)
df = get_data('^BVSP', start_date=inicio, end_date=fim)

df['close'].plot(color='k',lw=2,alpha=0.6)
df['med_mov']=df['close'].rolling(window=500,min_periods=0).mean()
df['med_mov'].plot(color='k',lw=3,style='--')

fig.grid()
fig.title('Ibovespa (2000-2022)',fontsize=18,weight='bold')
fig.legend(['Ibovespa','Média Móvel 500 dias'])




