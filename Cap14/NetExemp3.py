import networkx as nx
import matplotlib.pyplot as fig
import pandas as pd
import numpy as np

nodos = list(range(100))
df = pd.DataFrame({'De': np.random.choice(nodos,100),
                   'Para':np.random.choice(nodos,100)})

G = nx.from_pandas_edgelist(df, source='De',target='Para')
nx.draw(G, node_color='white', with_labels=True, font_weight='bold')
                 
fig.figure()

fig.hist([v for k,v in nx.degree(G)], color='grey')

