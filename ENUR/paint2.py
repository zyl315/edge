import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
xFont = {'weight': 'bold', 'size': 12}

is_save = False


def paint_rate(name: str, column_name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = "result/%s_%s.csv" % (name, i)
        file = pd.read_csv(path)
        res.append(list(file[column_name]))

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, res[0], linewidth=2, marker='*', color='green', label="Node 1")
    plt.plot(budget, res[1], linewidth=2, marker='.', color='red', label='Node 2')
    plt.plot(budget, res[2], linewidth=2, marker='v', color='skyblue', label='Node 3')
    plt.plot(budget, res[3], linewidth=2, marker='x', color='blue', label='Node 4')
    plt.plot(budget, res[4], linewidth=2, marker='p', color='gray', label='Node 5')
    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


def paint_utility(name: str, x_label, y_label, save_name):
    tmp = []
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = "result/%s_%s.csv" % (name, i)
        file = pd.read_csv(path)
        tmp.append((list(file["ac_utility"]), list(file['ep_utility'])))

    for t in tmp:
        list1 = []
        for i in range(len(t[0])):
            list1.append(t[0][i] / t[1][i])
        res.append(list1)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, res[0], linewidth=2, marker='*', color='green', label="Node 1")
    plt.plot(budget, res[1], linewidth=2, marker='.', color='red', label='Node 2')
    plt.plot(budget, res[2], linewidth=2, marker='v', color='skyblue', label='Node 3')
    plt.plot(budget, res[3], linewidth=2, marker='x', color='blue', label='Node 4')
    plt.plot(budget, res[4], linewidth=2, marker='p', color='gray', label='Node 5')
    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


def paint_budget(name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = "result/%s_%s.csv" % (name, i)
        file = pd.read_csv(path)
        res.append(list(file['budget_save']))

    index = np.array(budget)
    bar_width = 8
    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.bar(index - 2 * bar_width, res[0], width=bar_width, color='green', label='Node 1', edgecolor='black',
            hatch='////')
    plt.bar(index - 1 * bar_width, res[1], width=bar_width, color='red', label='Node 2', edgecolor='black',
            hatch="\\\\\\\\")
    plt.bar(index + 0 * bar_width, res[2], width=bar_width, color='skyblue', label='Node 3', edgecolor='black',
            hatch='/////')
    plt.bar(index + 1 * bar_width, res[3], width=bar_width, color='blue', label='Node 4', edgecolor='black',
            hatch="\\\\\\\\")
    plt.bar(index + 2 * bar_width, res[4], width=bar_width, color='orange', label='Node 5', edgecolor='black',
            hatch='/////')

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


def paint_average(column_name: str, x_label, y_label, average, save_name):
    res1 = []
    res2 = []
    budget = [_ for _ in range(200, 801, 50)]

    for i in range(0, 5):
        path1 = "result/result1_%s.csv" % i
        file1 = pd.read_csv(path1)
        res1.append(list(file1[column_name]))

        path2 = "result/result2_%s.csv" % i
        file2 = pd.read_csv(path2)
        res2.append(list(file2[column_name]))

    path3 = "result/result3_6.csv"
    file3 = pd.read_csv(path3)

    tmp1 = [0 for _ in range(0, 13)]
    tmp2 = [0 for _ in range(0, 13)]
    tmp3 = list(file3[column_name])

    for i in range(5):
        for j in range(len(res1[i])):
            tmp1[j] += (res1[i][j] / average)

        for j in range(len(res2[i])):
            tmp2[j] += (res2[i][j] / average)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, sorted(tmp1), linewidth=2, marker='*', color='green', label="BRD-ENUR")
    plt.plot(budget, sorted(tmp2), linewidth=2, marker='.', color='red', label='ENUR')
    plt.plot(budget, sorted(tmp3), linewidth=2, marker='v', color='skyblue', label='QIM')

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


def paint_average_budget(column_name: str, x_label, y_label, save_name):
    res1 = []
    res2 = []
    budget = [_ for _ in range(200, 801, 50)]

    for i in range(0, 5):
        path1 = "result/result1_%s.csv" % i
        file1 = pd.read_csv(path1)
        res1.append(list(file1[column_name]))

        path2 = "result/result2_%s.csv" % i
        file2 = pd.read_csv(path2)
        res2.append(list(file2[column_name]))

    path3 = "result/result3_6.csv"
    file3 = pd.read_csv(path3)

    tmp1 = [0 for _ in range(0, 13)]
    tmp2 = [0 for _ in range(0, 13)]
    tmp3 = list(file3[column_name])
    for i in range(5):
        for j in range(len(res1[i])):
            tmp1[j] += (res1[i][j])

        for j in range(len(res2[i])):
            tmp2[j] += (res2[i][j])

    index = np.array(budget)
    bar_width = 14
    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.bar(index - 1 * bar_width, tmp1, width=bar_width, color='green', label='BRD-ENUR',edgecolor='black',
            hatch='////')
    plt.bar(index + 0 * bar_width, tmp2, width=bar_width, color='red', label='ENUR',edgecolor='black',
            hatch='\\\\\\\\')
    plt.bar(index + 1 * bar_width, tmp3, width=bar_width, color='skyblue', label='QIM',edgecolor='black',
            hatch='////')

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


def paint_total_utility(column_name: str, column_name2, x_label, y_label, save_name):
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    budget = [_ for _ in range(200, 801, 50)]

    for i in range(0, 5):
        path1 = "result/result1_%s.csv" % i
        file1 = pd.read_csv(path1)
        res1.append(list(file1[column_name]))
        res3.append(list(file1[column_name2]))

        path2 = "result/result2_%s.csv" % i
        file2 = pd.read_csv(path2)
        res2.append(list(file2[column_name]))
        res4.append(list(file2[column_name2]))

    path3 = "result/result3_6.csv"
    file3 = pd.read_csv(path3)

    tmp1 = [0 for _ in range(0, 13)]
    tmp2 = [0 for _ in range(0, 13)]
    tmp3 = list(file3[column_name])
    tmp4 = [0 for _ in range(0, 13)]

    for i in range(5):
        for j in range(len(res1[i])):
            tmp1[j] += (res1[i][j])
        for j in range(len(res2[i])):
            tmp2[j] += (res2[i][j])
        for j in range(len(res1[i])):
            tmp4[j] += (res4[i][j])

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, sorted(tmp1), linewidth=2, marker='*', color='green', label="BRD-ENUR")
    plt.plot(budget, sorted(tmp2), linewidth=2, marker='.', color='red', label='ENUR')
    plt.plot(budget, tmp3, linewidth=2, marker='v', color='skyblue', label='QIM')
    # plt.plot(budget, tmp4, linewidth=0.84, marker='2', color='blue', label='Expected')
    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    if is_save:
        plt.savefig("res_flg/%s.png" % save_name, dpi=200)
    plt.show()


if __name__ == '__main__':
    # paint_rate("result1", "rate", "Budget", "Task accomplishment ratio", "fig4")
    # paint_rate("result1", "user_num", "Budget", "No. of selected users", "fig5")
    # paint_utility("result1", "Budget", "Normalized utility value", "fig6")
    # paint_budget("result1", "Budget", "Remaining budget", "fig7")

    # paint_rate("result2", "rate", "Budget", "Task accomplishment ratio", "fig8")
    # paint_rate("result2", "user_num", "Budget", "No. of selected users", "fig9")
    # paint_utility("result2", "Budget", "Normalized utility value", "fig10")
    # paint_budget("result2", "Budget", "Remaining budget", "fig11")

    paint_average("rate", "Budget", "Task accomplishment ratio", 5, "fig12")
    paint_average("user_num", "Budget", "No. of selected users", 1, "fig13")
    paint_total_utility("ac_utility", "ep_utility", "Budget", "Total utility value", "fig14")
    paint_average_budget("budget_save", "Budget", "Remaining budget", "fig15")
