import pandas as pd
import matplotlib.pyplot as fig
import seaborn as sns
import numpy as np
from scipy.stats import norm
from scipy.stats import stats
from math import log, sqrt, exp
from random import gauss
import matplotlib.ticker as ticker
import time
from matplotlib import cm
import matplotlib.dates as mdates
nome1='AM_neg'
nome2='km2'

eleic=pd.read_excel('deter_dia_AM.xlsx',sheet_name='Planilha1')
npts = 73
IntInicial=73
df=eleic[-IntInicial+0*npts:-0*IntInicial+0*3*npts-1]
df=df.reset_index()
df['med_mov_AM']=df[nome1].rolling(window=9,min_periods=0).mean()
df['med_mov_km']=df[nome2].rolling(window=9,min_periods=0).mean()
theta, beta, r_value, p_value, SE = stats.linregress(df[nome1],df[nome2])

ax1=fig.subplot(321)
ax1_dir=ax1.twinx()
ax1.plot(df.data,df[nome1],'-r')
ax1.legend([nome1,nome2])
ax1_dir.plot(df.data,df[nome2],'-b')
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=20))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))


fig.ylabel('TWITTER')
fig.grid
fig.title('AM neg x km2',fontsize=18)

ax2=fig.subplot(323)
ax2=sns.regplot(df[nome1],df[nome2],line_kws={'label':'$y=%3.7s*x+%3.7s$ $ SE=%3.7s$'%(theta, beta,SE)})
ax2.legend()

ax3=fig.subplot(322)
df[nome1].plot(kind='hist',density=True)
ax3=sns.kdeplot(df[nome1],cumulative=False).set(xlim=(0))

df[nome2].plot(kind='hist',density=True)
ax3=sns.kdeplot(df[nome2],cumulative=False).set(xlim=(0))
#ax3.legend([nome1,nome2])
fig.title('Densidade de Probabilidade - Twitter AM negativa x DETER(km2)')

ax4=fig.subplot(324)
pol=pd.concat([df[nome1],df[nome2]],axis=1)
ax4=sns.boxplot(data=pol, showfliers=False)
cor,pvalor=stats.ttest_rel(df[nome1].values,df[nome2].values)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax4.text(0.4,0.1,s='p< {:0.4f}'.format(pvalor),bbox=props,fontsize=13)
fig.setp(ax4.get_xticklabels(), visible=True)

ax5=fig.subplot(326)
ax5_dir=ax5.twinx()
cmap=cm.get_cmap('cividis')
ax5.plot(df.data,df['med_mov_AM'],color='red') 
ax5.fill_between(df.data,0,df['med_mov_AM'].values,cmap=cmap,alpha=0.1)
ax5_dir.plot(df.data,df['med_mov_km'],color='blue')
ax5_dir.fill_between(df.data,0,df['med_mov_km'].values,cmap=cmap,alpha=0.1)
ax5.legend(['med_twitter','med_km2'])
ax5.xaxis.set_major_locator(mdates.DayLocator(interval=20))
ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
#fig.gcf().autofmt_xdate()
####################### Cross-Correlacao ##############################

y1=np.array(df['med_mov_AM'][-npts:])
y2=np.array(df['med_mov_km'][-npts:])

lags = np.arange(-npts+2 , npts-1)
ccov = np.correlate(y1 - y1.mean(), y2 - y2.mean(), mode='full')
ccor = ccov / (npts * y1.std() * y2.std())

maxlag = lags[np.argmax(ccor)]
minlag = lags[np.argmin(ccor)]
signifmax = 2/sqrt(npts-abs(maxlag))
signifmin = 2/sqrt(npts-abs(minlag))

ax7=fig.subplot(325)
ax7.plot(lags, ccor,'-k',linewidth=3)
ax7.grid()
ax7.set_ylim(-0.5, 0.8)
ax7.set_ylabel('cross-correlação',fontsize=14,color='k',weight='bold')
ax7.set_xlabel('lag ',fontsize=14,color='k',weight='bold')

print("######### resultado da correlacao cruzada #############")
print("max correlation is at lag (dias) %d" % maxlag)
print("max correlation = %f" % ccor[np.argmax(ccor)])
print(" ")
print("valor de significancia = %f" % signifmax)
print("######### resultado da correlacao cruzada #############")
print("min correlation is at lag (dias) %d" % minlag)
print("min correlation = %f" % ccor[np.argmin(ccor)])
print(" ")
print("valor de significancia = %f" % signifmin)
print("######################################################")
      
########## Graficos para o artigo #######################
fig.figure()
 
art1=sns.lineplot(x=df.data,y=df[nome1],color='black',
                  label='tuites negativos/ dia keyword=amazonia',
                  linewidth=3)
art1.lines[0].set_linestyle('-')
art1.legend(loc='upper left')
art1.set_ylabel(art1.get_ylabel(), fontsize=18)
art1.set_xlabel(art1.get_xlabel(), fontsize=15)
art1.set(xlabel='data',ylabel='Keyword = "amazonia" - contagem tuites negativos / dia')
art2=fig.twinx()
art3=sns.lineplot(x=df.data, y=df[nome2],ax=art2, 
                  label='desmatamento real(km2) - DETER',
                  color='black',
                  linewidth=2)
art3.lines[0].set_linestyle('--')
leg=art3.legend()
leg_lines=leg.get_lines()
leg_lines[0].set_linestyle('--')
fig.gcf().autofmt_xdate()
art3.set_ylabel(art1.get_ylabel(), fontsize=18)
art3.set(ylabel='Desmatamento floresta amazônica em Km2 - DETER')

############ media movel para o artigo ###################
fig.figure()
art5=sns.lineplot(x=df.data,y=df['med_mov_AM'],color='black',
                  label='negative tweets mov. avg 7 days',
                  linewidth=3)
art5.lines[0].set_linestyle('-')
art5.legend(loc='upper left')
art5.set_ylabel(art1.get_ylabel(), fontsize=18)
art5.set_xlabel(art1.get_xlabel(), fontsize=15)
art5.set(xlabel='date',ylabel='Moving Average of negative tweets (7 days)')

art6=fig.twinx()
art7=sns.lineplot(x=df.data, y=df['med_mov_km'],ax=art6, 
                  label='Moving Average of deforestation (7 days)',
                  color='black',
                  linewidth=2)
art7.lines[0].set_linestyle('--')
leg=art7.legend()
leg_lines=leg.get_lines()
leg_lines[0].set_linestyle('--')
fig.gcf().autofmt_xdate()
art7.set_ylabel(art5.get_ylabel(), fontsize=18)
art7.set(ylabel='Moving Average Deforestation Amazon Forest Km2 (7days)')

###############  correlacao para artigo ################
fig.figure()
art8=fig.subplot(111)
art8.plot(lags, ccor,'-k',linewidth=3)
art8.set_ylim(-0.5, 0.8)
art8.set_ylabel('correlação cruzada',fontsize=14,color='k',weight='bold')
art8.set_xlabel('lag em dias',fontsize=14,color='k',weight='bold') 
fig.grid()
art8.text(x=-6,y=0.75,s='lag de 6 dias',fontsize=14,color='k',weight='bold')
art8.text(x=-6,y=0.68,s='*',fontsize=35,color='k',weight='bold')