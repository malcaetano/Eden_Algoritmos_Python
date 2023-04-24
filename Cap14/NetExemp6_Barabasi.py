import networkx as nx
import matplotlib.pyplot as fig
##############################################
# n eh o número de nodos
# m o número de arestas para cada novo nodo adicional
##############################################

G_peq_mundo = nx.barabasi_albert_graph(n=50, m=2)
nx.draw_circular(G_peq_mundo, node_color='white', with_labels=True, 
               font_weight='bold')               
fig.figure()
fig.hist([v for k,v in nx.degree(G_peq_mundo)], color='grey')

