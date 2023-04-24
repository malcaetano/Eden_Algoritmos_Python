import networkx as nx
import matplotlib.pyplot as fig

##############################################
# n eh o número de nodos
# m o número de arestas para cada novo nodo adicional
##############################################

#++++++++++++++ criacao da rede +++++++++++++++++
G_peq_mundo = nx.barabasi_albert_graph(n=50, m=2)  
#+++++++++++++ calculando cluster +++++++++++++++
aglomeracao=nx.clustering(G_peq_mundo)
print('cluster= ',aglomeracao)    # imprimindo clusters

aglomeracao=list(aglomeracao.values()) # transforma em lista para colorir
pos=nx.spring_layout(G_peq_mundo)      # posicao dos nodos
cmap=fig.cm.Wistia                     # colormap de cores
nodos=nx.draw_networkx_nodes(G_peq_mundo, pos, 
                             node_color=list(aglomeracao), 
                             with_labels=False,
                             font_weight='bold',
                             cmap=cmap)
#+++++++++++++++ barra de cores +++++++++++++++++++++++++++++++++++++++
fig.colorbar(nodos)
#+++++++++++++++ desenha as arestas entre os nodos ++++++++++++++++++++
arestas=nx.draw_networkx_edges(G_peq_mundo,pos)
#++++++++++++++  coloca os rotulos nos nodos +++++++++++++++++++++++++++++
rotulos=nx.draw_networkx_labels(G_peq_mundo,pos,font_weight='bold')

