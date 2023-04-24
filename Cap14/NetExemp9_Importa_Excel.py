import networkx as nx
import matplotlib.pyplot as fig
import pandas as pd

dados = pd.read_excel('Redes1.xlsx', sheet_name='Planilha1')
df = pd.DataFrame(dados)
G = nx.from_pandas_edgelist(df, source='De',target='Para')
#+++++++++++++ posicao dos nodos na rede ++++++++
pos=nx.spring_layout(G)
nodos=nx.nodes(G)
########### geracao da rede na figura ####################### 
nodos_rede=nx.draw_networkx_nodes(G, pos,
                             nodelist=nodos,
                             node_color='#FFFFCB')
arestas=nx.draw_networkx_edges(G,pos,
                               nodelist=nodos,
                               width=5.0, 
                               alpha=1,
                               edge_color='black')

nx.draw_networkx_labels(G,pos,font_weight='bold')



