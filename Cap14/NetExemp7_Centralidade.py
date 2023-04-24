import networkx as nx
import matplotlib.pyplot as fig
#++++++++++++++ criacao da rede +++++++++++++++++
G = nx.Graph()
G.add_node(0)
G.add_nodes_from([1,2,3])
G.add_edge(0,1)
G.add_edges_from([(1,2),(2,3),(3,1)])
#++++++++++++++ calculo da cenrralidade ++++++++++
centralidade=nx.betweenness_centrality(G)
cor_central=list(centralidade.values())
print('centralidade da rede = ',centralidade)
#+++++++++++++++ calculo das cores nos nodos com base na centralidade ++++
pos=nx.spring_layout(G)
cmap=fig.cm.Wistia    # <------------ barra em cor laranja
nodos=nx.draw_networkx_nodes(G, pos, 
                             node_color=cor_central, 
                             with_labels=False,
                             font_weight='bold',
                             cmap=cmap)
#+++++++++++++++ barra de cores +++++++++++++++++++++++++++++++++++++++
fig.colorbar(nodos)
#+++++++++++++++ desenha as arestas entre os nodos ++++++++++++++++++++
arestas=nx.draw_networkx_edges(G,pos)
#++++++++++++++  coloca os rotulos nos nodos +++++++++++++++++++++++++++++
rotulos=nx.draw_networkx_labels(G,pos,font_weight='bold',font_color='k')

