import networkx as nx
import matplotlib.pyplot as fig

########################################################
# n eh o número de nodos
# k o número de ligacoes proximas
# p a probabilidade de um nodo ser revisitado por um nodo distante
#######################################################

G_peq_mundo = nx.watts_strogatz_graph(n=100,k=5,p=0.4)
nx.draw_circular(G_peq_mundo, node_color='white', with_labels=True, 
               font_weight='bold')
fig.figure()
fig.hist([v for k,v in nx.degree(G_peq_mundo)], color='grey')

