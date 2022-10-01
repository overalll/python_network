import pandas as pd
def init_node(jiedian):
    data = pd.read_csv('large_twitch_features.csv')  # 读入csv文件
    col_1 = data['views']
    col_2 = data['mature']
    col_3 = data['life_time']
    col_4 = data['created_at']
    col_5 = data['updated_at']
    col_6 = data['numeric_id']
    col_7 = data['dead_account']
    col_8 = data['language']
    col_9 = data['affiliate']
    for i in range(len(data)):
        key = col_6[i]
        jiedian.setdefault(key, [])
        jiedian[key].append(col_1[i])
        jiedian[key].append(col_2[i])
        jiedian[key].append(col_3[i])
        jiedian[key].append(col_4[i])
        jiedian[key].append(col_5[i])
        jiedian[key].append(col_7[i])
        jiedian[key].append(col_8[i])
        jiedian[key].append(col_9[i])
    return


def print_node(jiedian):
    for j in range(len(jiedian)):
        print("id：{id}, views: {views}, mature: {mature}, life_time: {life_time},"
              "created_at: {created_at}, updated_at: {updated_at}, dead_account: {dead_account},"
              "language: {language}, affiliate: {affiliate}".format(id=j + 1,
                                                                    views=jiedian[j][0], mature=jiedian[j][1],
                                                                    life_time=jiedian[j][2], created_at=jiedian[j][3],
                                                                    updated_at=jiedian[j][4],
                                                                    dead_account=jiedian[j][5],
                                                                    language=jiedian[j][6], affiliate=jiedian[j][7]))
    return
