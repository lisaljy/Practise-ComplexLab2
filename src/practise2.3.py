import networkx as nx
import matplotlib.pyplot as plt
WS = nx.random_graphs.watts_strogatz_graph(20,4,0.3)
pos = nx.circular_layout(WS)
nx.draw(WS,pos,with_labels=False,node_size = 30)
#plt.show()
plt.savefig("WS.png")