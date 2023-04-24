#########################################################
# Classificador de Texto Baysesiano
#########################################################
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
import numpy as np

# Construcao das colunas para as classes de treinamentos
columns = ['sentenca', 'classes']
rows = []

# Frases para treinamentos
rows = [['O gato na mesa', 'animal'], 
        ['O cão na sala', 'animal'],
        ['A mesa na sala', 'não_animal'],
        ['O gato não é cão', 'animal'],
        ['gato e cão na sala', 'animal'],
        ['A sala não é mesa', 'não_animal']]

# +++++  Formatando dados para Treinamento ++++++++++++++++++++++++
treino = pd.DataFrame(rows, columns=columns)
print(' ')
print('---------------------------------')
print(treino)

# ++++ Criando a Matriz de Termos para "animais" +++++++++
frases_anim = [row['sentenca'] for index,row in treino.iterrows() if row['classes'] == 'animal']

vec_s = CountVectorizer()
X_s = vec_s.fit_transform(frases_anim)
materm_A = pd.DataFrame(X_s.toarray(), columns=vec_s.get_feature_names())
print(' ')
print('----------------------------------')
print('CLASSE "ANIMAIS" ')
print('----------------------------------')
print(materm_A)

#+++ Criando a Matriz de Termos para "nao animais" +++++++++++++
frases_na = [row['sentenca'] for index,row in treino.iterrows() if row['classes'] == 'não_animal']

vec_q = CountVectorizer()
X_q = vec_q.fit_transform(frases_na)
materm_Na = pd.DataFrame(X_q.toarray(), columns=vec_q.get_feature_names())

print(' ')
print('----------------------------------')
print('CLASSE "NÃO ANIMAIS" ')
print('----------------------------------')
print(materm_Na)

# Calculando a frequencia das palavras para classe "animais"
word_list_A = vec_s.get_feature_names();    
count_list_A = X_s.toarray().sum(axis=0) 
freq_A = dict(zip(word_list_A,count_list_A))
print(' ')
print('----------------------------------')
print('FREQUÊNCIA DAS PALAVRAS NA CLASSE "ANIMAIS" ')
print('----------------------------------')
print(freq_A)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

# Calculando a frequencia das palavras para classe "nao animais"
word_list_Na = vec_q.get_feature_names();    
count_list_Na = X_q.toarray().sum(axis=0) 
freq_Na = dict(zip(word_list_Na,count_list_Na))
print(' ')
print('----------------------------------')
print('FREQUÊNCIA DAS PALAVRAS NA CLASSE "NÃO ANIMAIS" ')
print('----------------------------------')

print(freq_Na)
    
####### Calculando a probabilidade para palavras na classe "animais" ########
from collections import Counter
totalFreq = dict(Counter(freq_A)+Counter(freq_Na)) # soma todas as frequencias
############################################################################

prob_A=[]
for word,count in zip(word_list_A,count_list_A):
    prob_A.append(count/totalFreq[word])
print(' ')
print('----------------------------------')
print('PROBABILIDADES DAS PALAVRAS NA CLASSE "ANIMAIS" ')
print('----------------------------------')
print(dict(zip(word_list_A,prob_A)))

####### Calculando a probabilidade para palavras na classe "nao animais"    
prob_Na=[]
for word,count in zip(word_list_Na,count_list_Na):
    prob_Na.append(count/totalFreq[word])
print(' ')
print('----------------------------------')
print('PROBABILIDADES DAS PALAVRAS NA CLASSE "NÃO ANIMAIS" ')
print('----------------------------------')
print(dict(zip(word_list_Na,prob_Na)))

#+++++ Colocando em vetor todas as palavras e suas probab. +++
docs = [row['sentenca'] for index,row in treino.iterrows()]

vec = CountVectorizer()
X = vec.fit_transform(docs)

#  total de caracteristicas
total_features = len(vec.get_feature_names())

total_caract_A = count_list_A.sum(axis=0)
total_caract_Na = count_list_Na.sum(axis=0)

############ nova sentenca ##################
print(' ')
print('----------------------------------')
print('SENTENÇA PARA TESTE ')
print('----------------------------------')
nova_frase = 'cão na mesa'
new_word_list = word_tokenize(nova_frase)
print(new_word_list)

######### probabilidades das palavras da frase nova na classe "animais" #####
prob_A_nova_palav = []
for word in new_word_list:
    if word in freq_A.keys():
        count = freq_A[word]
        prob_A_nova_palav.append(count/totalFreq[word])
    else:
        count = 0
        prob_A_nova_palav.append((count + 1)/(total_caract_A + total_features))
print(' ')
print('probabilidades das palavras da frase nova na classe "animais" ')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(dict(zip(new_word_list,prob_A_nova_palav)))

######### probabilidades das palavras da frase nova na classe "nao animais" #####
prob_Na_nova_palav = []
for word in new_word_list:
    if word in freq_Na.keys():
        count = freq_Na[word]
        prob_Na_nova_palav.append(count/totalFreq[word])
    else:
        count = 0
        prob_Na_nova_palav.append((count + 1)/(total_caract_Na + total_features))
print(' ')
print('probabilidades das palavras da frase nova na classe "não animais" ')
print(dict(zip(new_word_list,prob_Na_nova_palav)))

#######################################################
#        Calculo final de Bayes para classe "animais"
######################################################
prob_A=np.prod(prob_A_nova_palav)*(len(materm_A)/(len(materm_A)+len(materm_Na)))
print(' ')
print('############################################')
print('Prob Bayesiana da classe "animal" = ',prob_A )      

#######################################################
#        Calculo final de Bayes para classe "nao animais"
######################################################
prob_Na=np.prod(prob_Na_nova_palav)*(len(materm_Na)/(len(materm_A)+len(materm_Na)))
print(' ')
print('############################################')
print('Prob Bayesiana da classe "não animal" = ',prob_Na )  

#######################################################
#        Decisao Final
######################################################

print(' ')
print('#################### DECISÃO FINAL  ####################')
if prob_A>prob_Na:
      print('A sentença tem animal' )  
else:
      print('A sentença não tem animal' )       
