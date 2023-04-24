import pandas as pd
import matplotlib.pyplot as fig
import seaborn as sns
from scipy.stats import stats
####################### importacao d oExcel ##########################
df=pd.read_excel('Covid_UTI.xlsx',sheet_name='Planilha1')

###################### exclusao das datas ############################
df=df.reset_index()

##################### calculo dos coeficientes da regressao linear ###
theta, beta, r_value, p_value, SE = stats.linregress(df['internações'],df['uti'])

#################### grafico da regressao linear ####################
ax1=fig.figure()
ax1=sns.regplot(df['internações'],df['uti'],
                line_kws={'label':'$y=%3.7s*x+%3.7s$'%(theta, beta)},
                color='black')
ax1.legend()

################## comparacao dos histogramas #######################
fig.figure()
fig.subplot(211)
df['internações'].plot(kind='hist',density=True,color='gray',alpha=0.6)
sns.kdeplot(df['internações'],cumulative=False,color='black')
fig.subplot(212)
df['uti'].plot(kind='hist',density=True,color='gray',alpha=0.6)
sns.kdeplot(df['uti'],cumulative=False,color='black')

