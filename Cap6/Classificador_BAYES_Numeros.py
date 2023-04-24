#########################################################
# Classificador de Numeros Baysesiano
# Descobre se um conjunto tem somente numeros pares ou 
# somente numeros impares a partir de um treino
# 'sim': sao todos pares
# 'nao': sao todos impares
#########################################################
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Construcao das colunas para as classes de treinamentos
columns = ['c1','c2','c3','c4','c5','c6','classes']
rows = []

# Numeros para treinamentos
rows = [[2,10,12,16,46,60, 'sim'], 
        [3,13,31,35,39,59, 'não'],
        [5,39,43,47,51,57, 'não'],
        [8,18,22,26,28,34, 'sim'],
        [2,6,18,20,24,38, 'sim'],
        [1,21,31,37,39,45, 'não']]

# +++++  Formatando dados para Treinamento ++++++++++++++++++++++++
treino = pd.DataFrame(rows, columns=columns)
print(' ')
print('---------------------------------')
print(treino)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Cria a matriz de termos para 'sim', colocando todos os termos de pares e 
#impares separados para calcular a frequencia das aparicoes.
# Caso o numero apareca na classe 'sim' e nao apareca na classe 'nao' fica
# vazio a celula fica vazia. Para nao deixar aparecer vazio e substituir por
# zero, usa-se "fillna(0)" que preenche com zero campos vazios 'N.A.'
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
materm_A =treino[['c1','c2','c3','c4','c5','c6']].apply(pd.Series.value_counts,
                axis=1)[treino['classes']=='sim'].fillna(0)
materm_A =materm_A.loc[:,(materm_A!=0).any(axis=0)]
print(' ')
print('----------------------------------')
print('CLASSE "Sim" ')
print('----------------------------------')
print(materm_A)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Cria a matriz de termos para 'nao' e preenche vazios com 'fillna(0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
materm_Na = treino[['c1','c2','c3','c4','c5','c6']].apply(pd.Series.value_counts,
                  axis=1)[treino['classes']=='não'].fillna(0)
materm_Na=materm_Na.loc[:,(materm_Na!=0).any(axis=0)]
print(' ')
print('----------------------------------')
print('CLASSE "Não" ')
print('----------------------------------')
print(materm_Na)

# Calculando a frequencia dos numeros para classe "sim"
# Transfere os valores da matriz para uma lista

word_list_A = materm_A.columns.tolist()    
count_list_A = materm_A.sum() 
freq_A = materm_A.sum()
print(' ')
print('----------------------------------')
print('FREQUÊNCIA DOS NUMEROS NA CLASSE "Sim" ')
print('----------------------------------')
print(freq_A)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

# Calculando a frequencia dos numeros para classe "nao"
# Transfere os valores da matriz para uma lista

word_list_Na = materm_Na.columns.tolist()    
count_list_Na = materm_Na.sum()
freq_Na = materm_Na.sum()
print(' ')
print('----------------------------------')
print('FREQUÊNCIA DOS NUMEROS NA CLASSE "Não" ')
print('----------------------------------')

print(freq_Na)

####### Calculando a probabilidade dos numeros na classe "sim"

prob_A=[]
for count in count_list_A:
    prob_A.append(count/len(word_list_A))
print(' ')
print('----------------------------------')
print('PROBABILIDADE DOS NUMEROS NA CLASSE "Sim" ')
print('----------------------------------')
print(dict(zip(word_list_A,prob_A)))

####### Calculando a probabilidade dos numeros na classe "nao"    
prob_Na=[]
for count in count_list_Na:
    prob_Na.append(count/len(word_list_Na))
print(' ')
print('----------------------------------')
print('PROBABILIDADE DOS NUMEROS NA CLASSE "Não" ')
print('----------------------------------')
print(dict(zip(word_list_Na,prob_Na)))

#+++++ Colocando em vetor todas os numeros e suas probab. +++
docs = [row['classes'] for index,row in treino.iterrows()]

vec = CountVectorizer()
X = vec.fit_transform(docs)

#  total de caracteristicas
total_features = len(vec.get_feature_names())


total_caract_A = len(count_list_A)
total_caract_Na = len(count_list_Na)

############ nova sentenca ##################
print(' ')
print('----------------------------------')
print('CONJUNTO DE NUMEROS PARA TESTE ')
print('----------------------------------')
new_list = [1,5,7,11,13,25]

print(new_list)

######### probabilidades do novo conjunto de numeros para "sim" #####
prob_A_novo = []
for word in new_list:
    if word in freq_A.keys():
        count = freq_A[word]
    else:
        count = 0
    prob_A_novo.append((count + 1)/(total_caract_A + total_features))
print(' ')
print('probabilidades dos numeros do novo conjunto para a classe "sim" ')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(dict(zip(new_list,prob_A_novo)))



######### probabilidades do novo conjunto de numeros para "nao" #####
prob_Na_nova_palav = []
for word in new_list:
    if word in freq_Na.keys():
        count = freq_Na[word]
    else:
        count = 0
    prob_Na_nova_palav.append((count + 1)/(total_caract_Na + total_features))
print(' ')
print('probabilidades dos numeros do novo conjunto para a classe "não" ')
print(dict(zip(new_list,prob_Na_nova_palav)))

#######################################################
#        Calculo final de Bayes para classe "sim"
######################################################
prob_A=np.prod(prob_A_novo)*(len(materm_A)/(len(materm_A)+len(materm_Na)))
print(' ')
print('############################################')
print('Prob Bayesiana da classe "sim" = ',prob_A )      

#######################################################
#        Calculo final de Bayes para classe "nao"
######################################################
prob_Na=np.prod(prob_Na_nova_palav)*(len(materm_Na)/(len(materm_A)+len(materm_Na)))
print(' ')
print('############################################')
print('Prob Bayesiana da classe "não" = ',prob_Na )  

#######################################################
#        Decisao Final
######################################################

print(' ')
print('#################### DECISÃO FINAL  ####################')
if prob_A>prob_Na:
      print('sim' )  
else:
      print('não' )       
