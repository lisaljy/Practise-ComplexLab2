import networkx as nx
import matplotlib.pyplot as plt
a = open(r'c:\data.txt','r')
content = a.readlines()
city=[]
for line in content:
   group=line.strip()
   list = group.split('|')
   couple = [list[0],list[1]]
   city.append(couple)
G = nx.DiGraph()
G.add_edges_from(city)
pos = nx.random_layout(G)
nx.draw(G,pos,with_labels=True,node_size=30)
plt.savefig("data.png")
plt.show()

