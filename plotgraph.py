import matplotlib.pyplot as plt
import networkx as nx


def ego(g, rand):
    lista = g[rand - 1]
    G = nx.Graph()  #创建空图
    G.add_node(rand)    #中心节点
    for i_1 in lista:   #添加中心节点连结的点和他们之间的边
        G.add_node(i_1)
        G.add_edge(i_1, rand)
    for ii in lista:    #添加周围节点之间的边
        for i_2 in g[ii - 1]:
            if i_2 > ii and i_2 in lista:
                G.add_edge(ii, i_2)
    nx.draw(G, with_labels=True)
    plt.show()
    return
