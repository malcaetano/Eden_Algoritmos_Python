import networkx as nx
import matplotlib.pyplot as fig
import pandas as pd

dados = pd.read_excel('Redes3.xlsx', sheet_name='Planilha1')
df = pd.DataFrame(dados)
G = nx.from_pandas_edgelist(df, source='De',target='Para')
#+++++++++++++ posicao dos nodos na rede ++++++++
pos=nx.random_layout(G)
nodos=nx.nodes(G)
#+++++++++++++ calculo dos cliques ++++++++++++++
cliques=nx.find_cliques(G)
#+++++++++++++ separacao dos cliques acima de um valor ++++
cliques3 = [clq for clq in cliques if len(clq) >= 16]
#+++++++++++++ ordenacao dos nodos com cliques acima de um valor+++
nodes_cliq = set(n for clq in cliques3 for n in clq)
#++++++++++++ separacao e identificacao dos nodos com maiores graus
grau=nx.degree(G)
nod=[n for n in nodes_cliq if grau[n] >= 28]
#+++++++++++ escolha e separacao das arestas das comunidades para
#+++++++++++ colorir arestas com cores diferentes +++++++++++++++++
cores_arestas=[(v, w) for v, w in G.edges if v in nod]
cc1=nx.centrality.betweenness_centrality(G)          
################## desenhar a rede sem as comunidades ############ 
    
nodos=nx.draw_networkx_nodes(G, pos,
                             nodelist=nodos,
                             node_size=[v * 10000 for v in cc1.values()],
                             node_color='gray')
arestas=nx.draw_networkx_edges(G,pos,
                               nodelist=nodos,
                               width=1.0, 
                               alpha=0.3,
                               edge_color='black')

nx.draw_networkx_labels(G,pos,font_weight='bold',font_size=8)

################## colorir nodos e arestas das comunidades #######

nodos_comun= nx.draw_networkx_nodes(G, pos,
                       nodelist=nod,
                       node_color='tab:blue')
arestas_comun= nx.draw_networkx_edges(G, pos,
                       edgelist=cores_arestas,
                       width=5.0, 
                       alpha=1,
                       edge_color='black')
###################################################################

Eleic=df.plot(y='De',color='k',lw=3)
Eleic.set_ylabel('Lula', fontsize=16)
fig.grid()

