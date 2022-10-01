import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False


def show_shuxing(dt_views, mature_0, mature_1, \
           dt_life_time, dic_created, dic_updated, dead_account_0,\
           dead_account_1, dic_language, affiliate_0, affiliate_1):
    #绘制views统计结果
    x_data = [4, 8, 12, 15, 19, 27, 31, 35, 38]
    y_data = [0]*10
    for i_1 in range(10):
        y_data[i_1] = dt_views[i_1]
    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])
    plt.title('views')
    plt.xlabel('views个数范围,单位：百万')
    plt.ylabel('统计个数')
    plt.show()
    #绘制mature的统计结果
    x_mature = [mature_0, mature_1]
    plt.title('mature 0&1')
    plt.pie(x_mature, labels=['mature_0', 'mature_1'])
    plt.pie(x_mature)
    plt.show()
    #绘制lofe_time统计结果
    x_data = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
    y_data = dt_life_time
    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])
    plt.title('life_time')
    plt.xlabel('life_time范围,单位：百')
    plt.ylabel('统计个数')
    plt.show()
    #绘制created_time统计结果
    x_created_label = sorted(dic_created)
    x_created = [0]*len(x_created_label)
    for i in range(len(x_created_label)):
        x_created[i] = dic_created[x_created_label[i]]
    plt.pie(x_created, labels=x_created_label)
    plt.pie(x_created)
    plt.show()
    # 绘制updated_time统计结果
    x_updated_label = sorted(dic_updated)
    x_updated = [0] * len(x_updated_label)
    for i in range(len(x_updated_label)):
        x_updated[i] = dic_updated[x_updated_label[i]]
    plt.pie(x_updated, labels=x_updated_label)
    plt.pie(x_updated)
    plt.show()
    # 绘制dead_account的统计结果
    x_dead_account = [dead_account_0, dead_account_1]
    plt.title('dead_account 0&1')
    plt.pie(x_dead_account, labels=['dead_account0', 'dead_account_1'])
    plt.pie(x_dead_account)
    plt.show()
    # 绘制language统计结果
    x_language_label = sorted(dic_language)
    x_language = [0] * len(x_language_label)
    for i in range(len(x_language_label)):
        x_language[i] = dic_language[x_language_label[i]]
    plt.pie(x_language, labels=x_language_label)
    plt.title('language')
    plt.pie(x_language)
    plt.show()
    # 绘制affiliate的统计结果
    x_affiliate_account = [affiliate_0, affiliate_1]
    plt.title('affiliate 0&1')
    plt.pie(x_affiliate_account, labels=['affiliate_0', 'affiliate_1'])
    plt.pie(x_affiliate_account)
    plt.show()
    return
