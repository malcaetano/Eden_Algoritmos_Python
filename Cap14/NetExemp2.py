import networkx as nx
import matplotlib.pyplot as fig

G = nx.Graph()
G.add_node(0)
G.add_nodes_from([1,2,3])
G.add_edge(0,1)
G.add_edges_from([(1,2),(2,3),(3,1)])
nx.draw(G, node_color='white', with_labels=True, font_weight='bold')
fig.show()
A=nx.adjacency_matrix(G).todense()
print(A)
grau=G.degree([0,1,2,3])
print('grau do nodo A= ',grau)

