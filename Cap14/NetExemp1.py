import networkx as nx
import matplotlib.pyplot as fig

G = nx.Graph()
G.add_node('A')
G.add_nodes_from(['B','C','D','E'])
G.add_edges_from([('A','B'),('A','C'), ('B','D'), ('B','E'), ('C','E')])

nx.draw(G, node_color='white', with_labels=True, font_weight='bold')
fig.show()

A=nx.adjacency_matrix(G).todense()
print(A)

print('grau do nodo A= ',G.degree('A'))
