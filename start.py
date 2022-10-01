import numpy as np


def shuxing(g):
    # 求节点的度、节点数、平均度
    num_n = len(g)  #图中节点个数(g中无独立点）
    degree = 0
    degrees = [0] * num_n
    #计算无向图中每个节点的度
    for x_1 in range(len(g)):
        degree += len(g[x_1])
        degrees[x_1] += len(g[x_1])
    avdegree = degree / num_n  #平均度
    num_e = degree / 2  #无向图中边的个数是度的二分之一
    return num_n, num_e, avdegree


def tongji(jiedian):
    # 统计节点的属性分布
    max_views, mature_0, mature_1, max_life_time, dead_account_0, dead_account_1 = 0, 0, 0, 0, 0, 0
    affiliate_0, affiliate_1 = 0, 0
    created = {}
    updated = {}
    dic_language = {}
    #统计各节点属性的边界值或0，1型属性的个数
    for p in range(len(jiedian)):
        if jiedian[p][0] > max_views:  #views
            max_views = jiedian[p][0]
        if jiedian[p][1] == 0:  #mature
            mature_0 += 1
        if jiedian[p][1] == 1:
            mature_1 += 1
        if jiedian[p][2] > max_life_time:  #lifetime
            max_life_time = jiedian[p][2]
        o = jiedian[p][3].split('-')   #created-time
        if o[0] not in created:
            created[o[0]] = 1
        if o[0] in created:
            created[o[0]] += 1
        oo = jiedian[p][4].split('-')    #updated-time
        if oo[0] in updated:
            updated[oo[0]] += 1
        if oo[0] not in updated:
            updated[oo[0]] = 1
        if jiedian[p][5] == 0:   #dead-account
            dead_account_0 += 1
        if jiedian[p][5] == 1:
            dead_account_1 += 1
        if jiedian[p][6] in dic_language:   #language
            dic_language[jiedian[p][6]] += 1
        if jiedian[p][6] not in dic_language:
            dic_language[jiedian[p][6]] = 1
        if jiedian[p][7] == 0:    #affiliate
            affiliate_0 += 1
        if jiedian[p][7] == 1:
            affiliate_1 += 1
    list_views = np.linspace(0, max_views, 11)   #分成十组呈现统计结果
    dt_views = [0] * 10
    for y_1 in range(len(jiedian)):
        z_1 = jiedian[y_1][0]
        if z_1 < list_views[1]:
            dt_views[0] += 1
        elif z_1 < list_views[2] and z_1 > list_views[1]:
            dt_views[1] += 1
        elif z_1 < list_views[3] and z_1 > list_views[2]:
            dt_views[2] += 1
        elif z_1 < list_views[4] and z_1 > list_views[3]:
            dt_views[3] += 1
        elif z_1 < list_views[5] and z_1 > list_views[4]:
            dt_views[4] += 1
        elif z_1 < list_views[6] and z_1 > list_views[5]:
            dt_views[5] += 1
        elif z_1 < list_views[7] and z_1 > list_views[6]:
            dt_views[6] += 1
        elif z_1 < list_views[8] and z_1 > list_views[7]:
            dt_views[7] += 1
        elif z_1 < list_views[9] and z_1 > list_views[8]:
            dt_views[8] += 1
        else:
            dt_views[9] += 1
    list_life_time = np.linspace(0, max_life_time, 11)   #分成十组呈现统计结果
    dt_life_time = [0] * 10
    for y_2 in range(len(jiedian)):
        z_2 = jiedian[y_1][2]
        if z_2 < list_life_time[1]:
            dt_life_time[0] += 1
        elif z_2 < list_life_time[2] and z_2 > list_life_time[1]:
            dt_life_time[1] += 1
        elif z_2 < list_life_time[3] and z_2 > list_life_time[2]:
            dt_life_time[2] += 1
        elif z_2 < list_life_time[4] and z_2 > list_life_time[3]:
            dt_life_time[3] += 1
        elif z_2 < list_life_time[5] and z_2 > list_life_time[4]:
            dt_life_time[4] += 1
        elif z_2 < list_life_time[6] and z_2 > list_life_time[5]:
            dt_life_time[5] += 1
        elif z_2 < list_life_time[7] and z_2 > list_life_time[6]:
            dt_life_time[6] += 1
        elif z_2 < list_life_time[8] and z_2 > list_life_time[7]:
            dt_life_time[7] += 1
        elif z_2 < list_life_time[9] and z_2 > list_life_time[8]:
            dt_life_time[8] += 1
        else:
            dt_life_time[9] += 1
    dic_created = {}
    for key in created:
        key_n = int(key)
        dic_created[key_n] = created[key]
    dic_updated = {}
    for key in updated:
        key_n = int(key)
        dic_updated[key_n] = updated[key]
    return list_views, dt_views, mature_0, mature_1, list_life_time, \
           dt_life_time, dic_created, dic_updated, dead_account_0,\
           dead_account_1, dic_language, affiliate_0, affiliate_1