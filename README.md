# Practise-ComplexLab2
### 所用模块：   
[参考](http://blog.sciencenet.cn/blog-404069-337689.html)  
[Networks的例子](http://networkx.github.io/documentation/latest/examples/index.html)  

### 可视化（Drawing）：   
* 基本样式  
`node_size`:  指定节点的尺寸大小(默认是300)  
`node_color`:  指定节点的颜色 (默认是红色，可以用字符串简单标识颜色，例如'r'为红色，'b'为绿色等，具体可查看手册)  
`node_shape`:  节点的形状（默认是圆形，用字符串'o'标识，具体可查看手册）  
`alpha`: 透明度 (默认是1.0，不透明，0为完全透明)   
`width`: 边的宽度 (默认为1.0)  
`edge_color`: 边的颜色(默认为黑色)  
`style`: 边的样式(默认为实现，可选： solid|dashed|dotted,dashdot)  
`with_labels`: 节点是否带标签（默认为True）  
`font_size`: 节点标签字体大小 (默认为12)  
`font_color`: 节点标签字体颜色（默认为黑色）  
* 基本布局  
布局用pos参数指定  
circular_layout：节点在一个圆环上均匀分布  
random_layout：节点随机分布  
shell_layout：节点在同心圆上分布   
spring_layout： 用Fruchterman-Reingold算法排列节点   
spectral_layout：根据图的拉普拉斯特征向量排列节点   

### 复杂网络模型：  
* 规则图  
全局耦合网络：任意两个节点之间有边直接相连  
最近邻耦合网络：每一个节点只和它周围的邻居节点相连  
```
random_graphs.random_regular_graph(d, n)   
生成一个含有n个节点，每个节点有d个邻居节点的规则图  
```  
*可实现全局耦合&邻近耦合*  
星形耦合网络：有一个中心点，其余的N-1个点只与中心点相连，彼此不相连   
* ER随机图  
具有固定边数的ER随机图G(N,M)  
具有固定连边概率的ER随机图G(N,p)  
```
random_graphs.erdos_renyi_graph(n,p)  
生成一个含有n个节点、以概率p连接的ER随机图  
```  
*当N充分大时，所得边数会比较接近*  
* 小世界网络  
WS小世界模型：随机化重连  
*WS小世界模型是从完全规则网络向完全随机网络的过渡，在规则网络中引入少许随机性即可*  
```
random_graphs.watts_strogatz_graph(n, k, p)  
生成一个含有n个节点、每个节点有k个邻居、以概率p随机化重连边的WS小世界网络  
```  
NW小世界模型：随机化加边  
* 无标度网络模型   
BA无标度网络：节点增长，优先链接（针对www研究的有向化：新节点指向已有节点）  
```
random_graphs.barabasi_albert_graph(n, m)  
生成一个含有n个节点、每次加入m条边的BA无标度网络  
```  
Price 模型：针对论文引用网络的增长和累积优势机制  
节点复制模型：新加入的节点倾向于复制网络中已有节点的行为  
适应度模型：在BA模型的基础上提出，优先链接中，链接概率和每个节点的度和适应度之积成正比  
局域世界演化模型：在BA模型的基础上，优先链接机制针对每个节点各自的局域世界  

### Practice:  
将给定的城市编号进行有向图连边表示
