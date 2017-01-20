import networkx as nx
import matplotlib.pyplot as plt
RG = nx.random_graphs.random_regular_graph(3,20)
pos = nx.spectral_layout(RG)
nx.draw(RG,pos,with_labels=False,node_size = 30)
#plt.savefig("normal.png")
plt.show()