import matplotlib.pyplot as fig
import pandas as pd
import seaborn as sns
from scipy import stats

dados=pd.read_excel('Res_Corona_sensitividade.xlsx',sheet_name='Planilha1')
df=pd.DataFrame(dados)
df=df.set_index('data')

df['med_mov']=df['valor'].rolling(window=90,min_periods=0).mean()

ax=df[-4900:].plot(y=['valor','med_mov'],
     color=['xkcd:stone','black'])
fig.title('Monitoramento Sensitividade: [coronavirus+pneumonia]',fontsize=13)

fig.figure()
ax=df[len(df)-4900:len(df)-4500].valor.plot(kind='kde',color='black')
ax=df[-400:].valor.plot(kind='kde',color='black',linestyle="--")
fig.title('Monitoramento Sensitividade: [coronavirus+pneumonia]',fontsize=13)
fig.legend(['início','fim'])
fig.ylabel('DENSIDADE', fontsize=16)
fig.xlabel('SUBJETIVIDADE', fontsize=16)
fig.figure()
corona1=df[len(df)-4900:len(df)-4500].valor
corona1=corona1.reset_index()
del corona1['data']
corona1=corona1.rename(columns={'valor':'subj_in'})

corona2=df[-400:].valor
corona2=corona2.reset_index()
del corona2['data']
corona2=corona2.rename(columns={'valor':'subj_fim'})

corona=pd.concat([corona1,corona2],axis=1)
ax=sns.boxplot(data=corona)
cor,pvalor=stats.ttest_rel(corona['subj_in'].values,corona['subj_fim'].values)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0,0.7,s='início',bbox=props,fontsize=13)
ax.text(1,0.7,s='fim',bbox=props,fontsize=13)
ax.text(0.4,0.1,s='p< {:0.4f}'.format(pvalor),bbox=props,fontsize=13)
ax.yaxis.set_tick_params(labelsize=10)

print(stats.pearsonr(corona['subj_in'].values,corona['subj_fim'].values))


