import networkx as nx
import matplotlib.pyplot as fig
import pandas as pd
import seaborn as sns

fig.style.use('dark_background')

dados = pd.read_excel('Redes3.xlsx', sheet_name='Planilha1')
df1 = pd.DataFrame(dados)
df1=df1[-3500:]
G1 = nx.from_pandas_edgelist(df1, source='De',target='Para')
#+++++++++++++ posicao dos nodos na rede ++++++++
pos=pos=nx.random_layout(G1)
nodos=nx.nodes(G1)
#+++++++++++++ calculo dos cliques ++++++++++++++
cliques=nx.find_cliques(G1)
#+++++++++++++ separacao dos cliques acima de um valor ++++
cliques3 = [clq for clq in cliques if len(clq) >= 16]
#+++++++++++++ ordenacao dos nodos com cliques acima de um valor+++
nodes_cliq = set(n for clq in cliques3 for n in clq)
print(cliques3)
#++++++++++++ separacao e identificacao dos nodos com maiores graus
grau=nx.degree(G1)
nod=[n for n in nodes_cliq if grau[n] >= 29]
#+++++++++++ escolha e separacao das arestas das comunidades para
#+++++++++++ colorir arestas com cores diferentes +++++++++++++++++
cores_arestas=[(v, w) for v, w in G1.edges if v in nod]
cc1=nx.centrality.betweenness_centrality(G1)        
################## desenhar a rede sem as comunidades ############ 
    
nodos=nx.draw_networkx_nodes(G1, pos,
                             nodelist=nodos,
                             node_size=[v * 25000 for v in cc1.values()],
                             node_color='#FFFFCB')
arestas=nx.draw_networkx_edges(G1,pos,
                               nodelist=nodos,
                               width=1.0, 
                               alpha=0.1,
                               edge_color='white')

nx.draw_networkx_labels(G1,pos,font_weight='bold',font_size=8)

################## colorir nodos e arestas das comunidades #######

nodos_comun= nx.draw_networkx_nodes(G1, pos,
                       nodelist=nod,
                       node_color='tab:red')
arestas_comun= nx.draw_networkx_edges(G1, pos,
                       edgelist=cores_arestas,
                       width=2.0, 
                       alpha=0.5,
                       edge_color='tab:red')
###################################################################

dados = pd.read_excel('Redes4.xlsx', sheet_name='Planilha1')
df2 = pd.DataFrame(dados)
df2=df2[-3500:]
G2 = nx.from_pandas_edgelist(df2, source='De',target='Para')
#+++++++++++++ posicao dos nodos na rede ++++++++
pos=nx.random_layout(G2)
nodos=nx.nodes(G2)
#+++++++++++++ calculo dos cliques ++++++++++++++
cliques=nx.find_cliques(G2)
#+++++++++++++ separacao dos cliques acima de um valor ++++
cliques3 = [clq for clq in cliques if len(clq) >= 16]
#+++++++++++++ ordenacao dos nodos com cliques acima de um valor+++
nodes_cliq = set(n for clq in cliques3 for n in clq)
print(cliques3)
#++++++++++++ separacao e identificacao dos nodos com maiores graus
grau=nx.degree(G2)
#remove = [node for node,degree in dict(G2.degree()).items() if degree >=28]
#G2.remove_nodes_from(remove)
nod=[n for n in nodes_cliq if grau[n] >= 29]
#+++++++++++ escolha e separacao das arestas das comunidades para
#+++++++++++ colorir arestas com cores diferentes +++++++++++++++++
cores_arestas=[(v, w) for v, w in G2.edges if v in nod]
cc2=nx.centrality.betweenness_centrality(G2)          
################## desenhar a rede sem as comunidades ############ 
    
nodos=nx.draw_networkx_nodes(G2, pos,
                             nodelist=nodos,
                             node_size=[v * 25000 for v in cc2.values()],
                             node_color='#FFFFCB')
arestas=nx.draw_networkx_edges(G2,pos,
                               nodelist=nodos,
                               width=1.0, 
                               alpha=0.1,
                               edge_color='white')

nx.draw_networkx_labels(G2,pos,font_weight='bold',font_size=8)

################## colorir nodos e arestas das comunidades #######

nodos_comun= nx.draw_networkx_nodes(G2, pos,
                       nodelist=nod,
                       node_color='tab:blue')
arestas_comun= nx.draw_networkx_edges(G2, pos,
                       edgelist=cores_arestas,
                       width=2.0, 
                       alpha=0.5,
                       edge_color='tab:blue')
###################################################################
fig.axis('off')

######### grafico na disposicao do tempo ##########################
df2['mediaL']=df1['De'].rolling(window=60,min_periods=0).mean()
df2['mediaB']=df2['De'].rolling(window=60,min_periods=0).mean()

df2.plot(y=['mediaL','mediaB'],color=['tab:red','tab:blue'])
fig.title('média móvel de 60 minutos')
#+++++++++ comparando as centralidades +++++++++++++++++++++

df_nd1=pd.DataFrame.from_dict({'node1': list(cc1.keys()),
                              'centrality1': list(cc1.values())})
df_nd2=pd.DataFrame.from_dict({'node2': list(cc2.keys()),
                              'centrality2': list(cc2.values())})
fig.figure()

fig.subplot(211)
fig.title('Comparação entre as centralidades de intermediações dos nodos')
sns.barplot(data=df_nd1,x='node1',y='centrality1',color='tab:red')

fig.subplot(212)
sns.barplot(data=df_nd2,x='node2',y='centrality2',color='tab:blue')


####### transformando as centralidades em dataframe para achar o maximo nodo
####### para a primeira variavel
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
df_central1=df = pd.DataFrame.from_dict({'node': list(cc1.keys()),
                                         'centrality': list(cc1.values()) })
nd1,cent1 = df_central1.idxmax() #retorna o max nodo onde esta a max centralidade

####### descobre oa caminhos mais curtos ate o nodo da max centralidade
d1={}
for node in G1.nodes():
          d1[node]=nx.shortest_path_length(G1,df_central1['node'][cent1],node)


####### transformando as centralidades em dataframe para achar o maximo nodo
####### para a segunda variavel
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
df_central2=df = pd.DataFrame.from_dict({'node': list(cc2.keys()),
                                         'centrality': list(cc2.values()) })
nd2,cent2 = df_central2.idxmax() #retorna o nodo onde esta a max centralidade

####### descobre oa caminhos mais curtos ate o nodo da max centralidade
d2={}
for node in G2.nodes():
          d2[node]=nx.shortest_path_length(G2,df_central1['node'][cent2],node)

fig.figure()
sns.distplot(list(d1.values()),hist=False,color='tab:red') #  histograma da 1a centralidade
sns.distplot(list(d2.values()),hist=False,color='tab:blue') # histograma da 2a centralidade
fig.title('Frequências dos caminhos mais curtos até o nodo com máxima centralidade')
fig.xlabel('Comprimento dos caminhos mais curtos até o nodo central')