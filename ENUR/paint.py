import matplotlib.pyplot as plt
import numpy as np
from ENUR import data_dispose

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def paint_dot(position1, position2, position3, x_max=100, y_max=100):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.gca()
    ax.set_xticks(np.arange(0, x_max + 1, 5))
    ax.set_yticks(np.arange(0, y_max + 1, 5))

    x1 = list(map(lambda x: x[1], position1))
    y1 = list(map(lambda x: x[2], position1))
    plt.scatter(x1, y1)

    x1 = list(map(lambda x: x[1], position2))
    y1 = list(map(lambda x: x[2], position2))
    plt.scatter(x1, y1)

    x1 = list(map(lambda x: x[1], position3))
    y1 = list(map(lambda x: x[2], position3))
    plt.scatter(x1, y1)

    plt.rc('grid', linestyle="-", color='black')
    plt.grid()
    plt.show()


def paint_broken_line(filename, round_, column_name, y_label):
    budget = [200, 300, 400, 500, 600, 700, 800]
    data1 = data_dispose.get_result(filename, round_)

    res = []
    for j in range(round_):
        tmp_list = []
        for i in range(200, 801, 100):
            tmp = data1[i][j][column_name]
            tmp_list.append(tmp)
        res.append(tmp_list)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, res[0], color='green', label="Node-1", marker='o')
    plt.plot(budget, res[1], color='red', label='Node-2', marker='*')
    plt.plot(budget, res[2], color='skyblue', label='Node-3', marker='x')
    plt.plot(budget, res[3], color='blue', label='Node-4', marker='+')
    plt.plot(budget, res[4], color='gray', label='Node-5', marker='4')
    plt.legend()  # 显示图例

    plt.xlabel('Budget')
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


def paint_tiao_xing1(filename, round_):
    budget = [200, 300, 400, 500, 600, 700, 800]
    data1 = data_dispose.get_result(filename, round_)

    index = np.array(budget)
    res = []
    for j in range(round_):
        tmp_list = []
        for i in range(200, 801, 100):
            tmp = data1[i][j]['budget_save']
            tmp_list.append(tmp)
        res.append(tmp_list)

    bar_width = 15
    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.bar(index - 2 * bar_width, res[0], width=bar_width, color='green', label='Node-1')
    plt.bar(index - 1 * bar_width, res[1], width=bar_width, color='gray', label='Node-2')
    plt.bar(index + 0 * bar_width, res[2], width=bar_width, color='skyblue', label='Node-3')
    plt.bar(index + 1 * bar_width, res[3], width=bar_width, color='blue', label='Node-4')
    plt.bar(index + 2 * bar_width, res[4], width=bar_width, color='orange', label='Node-5')

    plt.ylabel('Budget surplus')
    plt.xlabel('Budget')
    plt.legend()
    plt.show()


def paint_broken_line2(round_, column_name, y_label):
    budget = [200, 300, 400, 500, 600, 700, 800]
    data1 = data_dispose.get_result('result11.csv', round_)
    data2 = data_dispose.get_result('result22.csv', round_)
    data3 = data_dispose.get_result3('result33.csv')

    res1 = []
    res2 = []
    for i in range(200, 801, 100):
        tmp_list1 = []
        tmp_list2 = []
        for j in range(_round):
            tmp1 = data1[i][j][column_name]
            tmp2 = data2[i][j][column_name]
            tmp_list1.append(tmp1)
            tmp_list2.append(tmp2)
        res1.append(tmp_list1)
        res2.append(tmp_list2)

    y1 = []
    y2 = []
    y3 = data3[column_name]
    for i in range(len(res1)):
        y1.append(sum(res1[i]) / len(res1[i]))
        y2.append(sum(res2[i]) / len(res2[i]))

    print(res1)
    print(len(res1))

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, y1, color='green', label="Our-online", marker='o')
    plt.plot(budget, y2, color='red', label='Our-offline', marker='*')
    plt.plot(budget, y3, color='skyblue', label='QIM', marker='x')
    plt.legend()  # 显示图例

    plt.xlabel('Budget')
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


def paint_broken_line3(round_, column_name, y_label):
    budget = [200, 300, 400, 500, 600, 700, 800]
    data1 = data_dispose.get_result('result11.csv', round_)
    data2 = data_dispose.get_result('result22.csv', round_)
    data3 = data_dispose.get_result3('result33.csv')

    res1 = []
    res2 = []
    for i in range(200, 801, 100):
        tmp_list1 = []
        tmp_list2 = []
        for j in range(_round):
            tmp1 = data1[i][j][column_name]
            tmp2 = data2[i][j][column_name]
            tmp_list1.append(tmp1)
            tmp_list2.append(tmp2)
        res1.append(tmp_list1)
        res2.append(tmp_list2)

    y1 = []
    y2 = []
    y3 = data3[column_name]
    for i in range(len(res1)):
        y1.append(sum(res1[i]))
        y2.append(sum(res2[i]))

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, y1, color='green', label="Our-online", marker='o')
    plt.plot(budget, y2, color='red', label='Our-offline', marker='*')
    plt.plot(budget, y3, color='skyblue', label='QIM', marker='x')
    plt.legend()  # 显示图例

    plt.xlabel('Budget')
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


def paint_tiao_xing3(round_, column_name, y_label):
    budget = [200, 300, 400, 500, 600, 700, 800]
    data1 = data_dispose.get_result('result11.csv', round_)
    data2 = data_dispose.get_result('result22.csv', round_)
    data3 = data_dispose.get_result3('result33.csv')

    index = np.array(budget)
    res1 = []
    res2 = []
    for i in range(200, 801, 100):
        tmp_list1 = []
        tmp_list2 = []
        for j in range(_round):
            tmp1 = data1[i][j][column_name]
            tmp2 = data2[i][j][column_name]
            tmp_list1.append(tmp1)
            tmp_list2.append(tmp2)
        res1.append(tmp_list1)
        res2.append(tmp_list2)

    y1 = []
    y2 = []
    y3 = data3[column_name]
    for i in range(len(res1)):
        y1.append(sum(res1[i]))
        y2.append(sum(res2[i]))

    bar_width = 20
    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.bar(index - 1 * bar_width, y1, width=bar_width, color='green', label='Our-online')
    plt.bar(index - 0 * bar_width, y2, width=bar_width, color='red', label='Our-offline')
    plt.bar(index + 1 * bar_width, y3, width=bar_width, color='skyblue', label='QIM')

    plt.ylabel(y_label)
    plt.xlabel('Budget')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    _round = 5
    # paint_broken_line('result11.csv', _round, 'average_rate', 'Task accomplish ratio')
    # paint_broken_line('result11.csv', _round, 'user_num', 'NO. of selected users')
    # paint_tiao_xing1('result11.csv', _round)
    # paint_broken_line('result22.csv', _round, 'average_rate', 'Task accomplish ratio')
    # paint_broken_line('result22.csv', _round, 'user_num', 'NO. of selected users')
    # paint_tiao_xing1('result22.csv', _round)
    paint_broken_line2(_round, 'average_rate', 'Task accomplish ratio')
    paint_broken_line3(_round, 'user_num', 'NO. of selected users')
    paint_tiao_xing3(_round, 'budget_save', 'Budget surplus')

    # paint()
