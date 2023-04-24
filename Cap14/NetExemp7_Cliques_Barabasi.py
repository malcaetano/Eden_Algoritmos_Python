import networkx as nx
import matplotlib.pyplot as fig

##############################################
# n eh o número de nodos
# m o número de arestas para cada novo nodo adicional
##############################################

#++++++++++++++ criacao da rede +++++++++++++++++
G_peq_mundo = nx.barabasi_albert_graph(n=50, m=2)  
#+++++++++++++ posicao dos nodos na rede ++++++++
pos=nx.spring_layout(G_peq_mundo)
nodos=nx.nodes(G_peq_mundo)
#+++++++++++++ calculo dos cliques ++++++++++++++
cliques=nx.find_cliques(G_peq_mundo)
#+++++++++++++ separacao dos cliques acima de um valor ++++
cliques3 = [clq for clq in cliques if len(clq) >= 3]
#+++++++++++++ ordenacao dos nodos com cliques acima de um valor+++
nodes_cliq = set(n for clq in cliques3 for n in clq)
#++++++++++++ separacao e identificacao dos nodos com maiores graus
grau=nx.degree(G_peq_mundo)
nod=[n for n in nodes_cliq if grau[n] >= 10]
#+++++++++++ escolha e separacao das arestas das comunidades para
#+++++++++++ colorir arestas com cores diferentes +++++++++++++++++
cores_arestas=[(v, w) for v, w in G_peq_mundo.edges if v in nod]
        
################## desenhar a rede sem as comunidades ############       
nodos=nx.draw_networkx_nodes(G_peq_mundo, pos,
                             nodelist=nodos,
                             node_color='tab:red')
arestas=nx.draw_networkx_edges(G_peq_mundo,pos,
                               nodelist=nodos,
                               width=5.0, 
                               alpha=0.3,
                               edge_color='black')

################## colorir nodos e arestas das comunidades #######

nodos_comun= nx.draw_networkx_nodes(G_peq_mundo, pos,
                       nodelist=nod,
                       node_color='tab:blue')
arestas_comun= nx.draw_networkx_edges(G_peq_mundo, pos,
                       edgelist=cores_arestas,
                       width=5.0, 
                       alpha=1,
                       edge_color='black')
###################################################################

