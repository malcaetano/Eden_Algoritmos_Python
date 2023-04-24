# Regressão Linear e coef.correlação
import matplotlib.pyplot as fig
import numpy as np
from scipy import stats

col1=[0,0.5,1,2,3,4,5]
col2=[5,1,2,4,6,8,10]

#+++++++++++++++++ Transforma lista em vetor
dados1=np.array(col1)
dados2=np.array(col2)    

#+++++++++++++ Regressão Linear +++++++++++++++++++++++++++++++
beta,beta0,r_value,p_value,std_err=stats.linregress(dados1,dados2)
print('+++++++++++++++++++ REGRESSÃO LINEAR +++++++++++++++')
print(' beta         beta0    r_value  p_value  std_err')
yLin = beta*dados1 + beta0
print('%10.6f %10.6f %5.2f %10.6f %10.8f' % (beta,beta0,r_value,p_value,std_err))

fig.plot(dados1,yLin,'-k',dados1,dados2,'ok')
fig.xlabel('dados1',fontsize=14)
fig.ylabel('dados2',fontsize=14)
#+++++++++++++ correlação +++++++++++++++++++++++++++++++
cor,pval = stats.pearsonr(dados1,dados2)    
#fig.text(87000,18,'r = ',fontsize=14)
#fig.text(90000,18,str(cor),fontsize=14)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('correlação      p-value')
print(cor,pval)    


        
    

   

    

       
        
