import pandas as pd
import matplotlib.pyplot as fig
import seaborn as sns

df=pd.read_excel('TesteNuclear.xlsx',
                  sheet_name='Dados')

df=pd.DataFrame(df)
df.index=df['data']
df=df.drop(['data'],axis=1)

figura, ax = fig.subplots()

ax=df['Temperatura'].plot(ylabel='TEMPERATURA',
     legend=True,color='black',linewidth=3)

ax.yaxis.tick_left()
fig.xticks(df.index[::10],rotation=30)
ax.legend(loc='upper left',prop= {'weight':'bold'})
fig.title('AQUECIMENTO GLOBAL')

ax_1=ax.twinx()
ax_1.spines['right'].set_position(('axes', 1))
ax_1=df['CO2_Var_abs'].plot(ylabel='Var Co2',legend=True,
       color='black',alpha=0.8,style='-.')
ax_1.legend(bbox_to_anchor=(0.3, 1),prop= {'weight':'bold'})
ax_1.yaxis.set_label_position("right")
ax_1.yaxis.set_label_coords(1.02,0.5)

df['minCo2']=df['CO2_Var_abs'].rolling(window=50).min()
df['medCo2']=df['CO2_Var_abs'].rolling(window=50).mean()
df['maxCo2']=df['CO2_Var_abs'].rolling(window=50).max()
Co2=df[['minCo2','medCo2','maxCo2']].copy()
Co2=Co2.dropna()

figura,ax=fig.subplots()
ax.plot(Co2['medCo2'].values[::9],color='black',linewidth=4)
Co2[::10].T.boxplot(color='black')
fig.title('Variação emissão absoluta CO2 --- Boxplot média móvel = 50 anos',
          fontsize=20)

