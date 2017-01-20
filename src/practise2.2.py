import networkx as nx
import matplotlib.pyplot as plt
ER = nx.random_graphs.erdos_renyi_graph(20,0.2)
pos = nx.shell_layout(ER)
nx.draw(ER,pos,with_labels=False,node_size = 30)
#plt.show()
plt.savefig("ER.png")