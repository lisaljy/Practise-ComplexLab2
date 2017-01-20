import networkx as nx
import matplotlib.pyplot as plt
BA = nx.random_graphs.barabasi_albert_graph(20,1)
pos = nx.spring_layout(BA)
nx.draw(BA,pos,with_labels=False,node_size = 30)
plt.savefig("BA.png")