import pandas as pd


def init_graph(g, start_edges, end_edges):
    '''
    :param g: 图，一个双层索引列表，存储对应节点所连接的所有节点id
    :param start_edges: 边的起始点
    :param end_edges: 边的终止点
    '''
    data_1 = pd.read_csv('large_twitch_edges.csv')
    st_ed = data_1['numeric_id_1']
    en_ed = data_1['numeric_id_2']
    for i in range(len(data_1)):
        edge1 = st_ed[i]
        edge2 = en_ed[i]
        start_edges[i] = edge1
        end_edges[i] = edge2
    for l in range(len(start_edges)):     #构建一个索引表，如3和1之间有边，则g[0]有3，g[2]有1
        if start_edges[l] not in g[end_edges[l] - 1]:
            g[end_edges[l] - 1].append(start_edges[l])
        if end_edges[l] not in g[start_edges[l] - 1]:
            g[start_edges[l] - 1].append(end_edges[l])
    return