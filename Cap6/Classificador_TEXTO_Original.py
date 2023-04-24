#########################################################
# Classificador de Texto Baysesiano
#########################################################
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
import numpy as np

# Construcao das colunas para as classes de treinamentos
columns = ['sent', 'class']
rows = []

# Frases para treinamentos
rows = [['This is my book', 'stmt'], 
        ['They are novels', 'stmt'],
        ['have you read this book', 'question'],
        ['who is the author', 'question'],
        ['what are the characters', 'question'],
        ['This is how I bought the book', 'stmt'],
        ['I like fictions', 'stmt'],
        ['what is your favorite book', 'question']]

# +++++  Formatando dados para Treinamento ++++++++++++++++++++++++
training_data = pd.DataFrame(rows, columns=columns)
print(training_data)

# ++++ Criando a Matriz de Termos "afirmacao" +++++++++
stmt_docs = [row['sent'] for index,row in training_data.iterrows() if row['class'] == 'stmt']

vec_s = CountVectorizer()
X_s = vec_s.fit_transform(stmt_docs)
tdm_s = pd.DataFrame(X_s.toarray(), columns=vec_s.get_feature_names())

print(tdm_s)

#+++ Criando a Matriz de Termos "questoes +++++++++++++
q_docs = [row['sent'] for index,row in training_data.iterrows() if row['class'] == 'question']

vec_q = CountVectorizer()
X_q = vec_q.fit_transform(q_docs)
tdm_q = pd.DataFrame(X_q.toarray(), columns=vec_q.get_feature_names())

print(tdm_q)

# Calculando a frequencia das palavras para "afirmacao"
word_list_s = vec_s.get_feature_names();    
count_list_s = X_s.toarray().sum(axis=0) 
freq_s = dict(zip(word_list_s,count_list_s))
print(freq_s)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

# Calculando a frequencia das palavras para "questoes"
word_list_q = vec_q.get_feature_names();    
count_list_q = X_q.toarray().sum(axis=0) 
freq_q = dict(zip(word_list_q,count_list_q))
print('+++++++++++++++++++++++++++++++++')
print(freq_q)

####### Calculando a probabilidade para "afirmacao"
prob_s=[]
for word,count in zip(word_list_s,count_list_s):
    prob_s.append(count/len(word_list_s))
print('+++++++++++++++++++++++++++++++++')
print(dict(zip(word_list_s,prob_s)))

####### Calculando a probabilidade para "questoes"    
prob_q=[]
for count in count_list_q:
    prob_q.append(count/len(word_list_q))
print(' ')    
print('+++++++++++++++++++++++++++++++++')
print(dict(zip(word_list_q,prob_q)))

#+++++ Colocando em vetor todas as palavras e suas probab. +++
docs = [row['sent'] for index,row in training_data.iterrows()]

vec = CountVectorizer()
X = vec.fit_transform(docs)

#  total de caracteristicas
total_features = len(vec.get_feature_names())
print(total_features)

total_cnts_features_s = count_list_s.sum(axis=0)
total_cnts_features_q = count_list_q.sum(axis=0)

############ nova sentenca ##################
new_sentence = 'what is the price of the book'
new_word_list = word_tokenize(new_sentence)
print(new_word_list)

######### probabilidades das palavras da sentenca para "afirmacao" #####
prob_s_with_ls = []
for word in new_word_list:
    if word in freq_s.keys():
        count = freq_s[word]
    else:
        count = 0
    prob_s_with_ls.append((count + 1)/(total_cnts_features_s + total_features))
print(' ')
print('++++++++++++++++++++')
print(dict(zip(new_word_list,prob_s_with_ls)))



######### probabilidades das palavras da sentenca para "questao" #####
prob_q_with_ls = []
for word in new_word_list:
    if word in freq_q.keys():
        count = freq_q[word]
    else:
        count = 0
    prob_q_with_ls.append((count + 1)/(total_cnts_features_q + total_features))
print(' ')
print('++++++++++++++++++++')
print(dict(zip(new_word_list,prob_q_with_ls)))

#######################################################
#        Calculo final de Bayes para "afirmativo"
######################################################
probA=np.prod(prob_s_with_ls)*(len(tdm_s)/(len(tdm_s)+len(tdm_q)))
print('############################################')
print('Prob Bayesiana "afirmação" = ',probA )      

#######################################################
#        Calculo final de Bayes para "questao"
######################################################
probQ=np.prod(prob_q_with_ls)*(len(tdm_q)/(len(tdm_s)+len(tdm_q)))
print('############################################')
print('Prob Bayesiana "questao" = ',probQ )  

#######################################################
#        Decisao Final
######################################################

print(' ')
print('#################### DECISÃO FINAL  ####################')
if probA>probQ:
      print('A sentença é uma afirmação' )  
else:
      print('A sentença é uma questão' )       
