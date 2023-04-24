import networkx as nx
import matplotlib.pyplot as fig

##############################################
# n eh o número de nodos
# m o número de arestas para cada novo nodo adicional
##############################################

#++++++++++++++ criacao da rede +++++++++++++++++
G_peq_mundo = nx.barabasi_albert_graph(n=50, m=2)  
#++++++++++++++ calculo da cenrralidade ++++++++++
centralidade=nx.betweenness_centrality(G_peq_mundo)
cor_central=list(centralidade.values())
print('centralidade máxima da rede = ',max(centralidade.values()))

#+++++++++++++++ calculo das cores nos nodos com base na centralidade ++++
pos=nx.spring_layout(G_peq_mundo)
cmap=fig.cm.Wistia
nodos=nx.draw_networkx_nodes(G_peq_mundo, pos, 
                             node_color=cor_central,
                             cmap=cmap)
#+++++++++++++++ barra de cores +++++++++++++++++++++++++++++++++++++++
fig.colorbar(nodos)
#+++++++++++++++ desenha as arestas entre os nodos ++++++++++++++++++++
arestas=nx.draw_networkx_edges(G_peq_mundo,pos)
#++++++++++++++  coloca os rotulos nos nodos +++++++++++++++++++++++++++++
rotulos=nx.draw_networkx_labels(G_peq_mundo,pos,font_weight='bold')

caminho_medio=nx.average_shortest_path_length(G_peq_mundo)
diametro= nx.diameter(G_peq_mundo)
print(' ')
print('caminho médio = ',caminho_medio)
print('diâmetro = ', diametro)


