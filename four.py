from work4.GraphStat.Graph.node import init_node
from work4.GraphStat.Graph.node import print_node
from work4.GraphStat.Graph.graph import init_graph
from work4.GraphStat.Graph.start import shuxing
from work4.GraphStat.Graph.start import tongji
from work4.GraphStat.Visualization.plotgraph import ego
from work4.GraphStat.Visualization.plotnodes import show_shuxing


def main():
    jiedian = {}
    start_edges = []
    end_edges = []
    init_node(jiedian)
    print_node(jiedian)
    start_edges = [0] * 6797557
    end_edges = [0] * 6797557
    g = [[] for k in range(len(jiedian))]
    init_graph(g, start_edges, end_edges)
    print('图中与第一个节点有边联系的节点有：')
    print(g[0])
    num_n, num_e, avdegree = shuxing(g)
    print(num_n)
    print(num_e)
    print(avdegree)
    list_views, dt_views, mature_0, mature_1, list_life_time, \
    dt_life_time, dic_created, dic_updated, dead_account_0, \
    dead_account_1, dic_language, affiliate_0, affiliate_1 = tongji(jiedian)
    print(dic_language)
    rand = 98343
    ego(g, rand)
    show_shuxing(dt_views, mature_0, mature_1, \
                 dt_life_time, dic_created, dic_updated, dead_account_0, \
                 dead_account_1, dic_language, affiliate_0, affiliate_1)
    return


main()

