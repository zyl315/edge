import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
xFont = {'weight': 'bold', 'size': 12}

is_save = True
dpi = 200
figsize = (4, 3.2)
fontsize = 12
linewidth = 2
file_path = "../data/ENUR/result%s.csv"
save_path = "../results/fig/%s.png"


def paint_rate(name: str, column_name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = file_path % name
        file = pd.read_csv(path)
        file = file[file['node_id'] == i]
        res.append(list(file[column_name]))

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(budget, res[0], linewidth=linewidth, marker='*', color='green', label="Node 1")
    plt.plot(budget, res[1], linewidth=linewidth, marker='.', color='red', label='Node 2')
    plt.plot(budget, res[2], linewidth=linewidth, marker='v', color='skyblue', label='Node 3')
    plt.plot(budget, res[3], linewidth=linewidth, marker='x', color='blue', label='Node 4')
    plt.plot(budget, res[4], linewidth=linewidth, marker='p', color='gray', label='Node 5')
    plt.legend(fontsize=fontsize - 2)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    if is_save:
        plt.savefig(save_path % save_name, dpi=dpi)
    plt.show()


def paint_utility(name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = file_path % name
        file = pd.read_csv(path)
        file = file[file['node_id'] == i]
        list1 = list(file['ac_utility'] / file['ep_utility'])
        res.append(list1)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(budget, res[0], linewidth=linewidth, marker='*', color='green', label="Node 1")
    plt.plot(budget, res[1], linewidth=linewidth, marker='.', color='red', label='Node 2')
    plt.plot(budget, res[2], linewidth=linewidth, marker='v', color='skyblue', label='Node 3')
    plt.plot(budget, res[3], linewidth=linewidth, marker='x', color='blue', label='Node 4')
    plt.plot(budget, res[4], linewidth=linewidth, marker='p', color='gray', label='Node 5')
    plt.legend(fontsize=fontsize - 2)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    if is_save:
        plt.savefig(save_path % save_name, dpi=dpi)
    plt.show()


def paint_budget(name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = file_path % name
        file = pd.read_csv(path)
        file = file[file['node_id'] == i]
        res.append(list(file['budget_save']))

    index = np.array(budget)
    bar_width = 8
    plt.figure(figsize=figsize, dpi=dpi)
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

    plt.legend(fontsize=fontsize - 2)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    if is_save:
        plt.savefig(save_path % save_name, dpi=dpi)
    plt.show()


def paint_line(column_name: str, x_label, y_label, average, save_name):
    res1, res2, res3, budget = data(column_name, average)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(budget, res1, linewidth=linewidth, marker='*', color='green', label="BRD-ENUR")
    plt.plot(budget, res2, linewidth=linewidth, marker='.', color='red', label='ENUR')
    plt.plot(budget, res3, linewidth=linewidth, marker='v', color='skyblue', label='QIM')

    plt.legend(fontsize=fontsize - 2)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    if is_save:
        plt.savefig(save_path % save_name)
    plt.show()


def paint_bar(column_name: str, x_label, y_label, save_name):
    res1, res2, res3, budget = data(column_name, False)
    index = np.array(budget)
    bar_width = 14
    plt.figure(figsize=figsize, dpi=dpi)
    plt.bar(index - 1 * bar_width, res1, width=bar_width, color='green', label='BRD-ENUR', edgecolor='black',
            hatch='////')
    plt.bar(index + 0 * bar_width, res2, width=bar_width, color='red', label='ENUR', edgecolor='black',
            hatch='\\\\\\\\')
    plt.bar(index + 1 * bar_width, res3, width=bar_width, color='skyblue', label='QIM', edgecolor='black',
            hatch='////')

    plt.legend(fontsize=fontsize - 2)

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    if is_save:
        plt.savefig(save_path % save_name, dpi=dpi)
    plt.show()


def data(column_name, average):
    res1 = []
    res2 = []
    budget = [_ for _ in range(200, 801, 50)]
    for b in budget:
        file1 = pd.read_csv(file_path % 1)
        list1 = list(file1[file1['budget'] == b][column_name])

        file2 = pd.read_csv(file_path % 2)
        list2 = list(file2[file2['budget'] == b][column_name])

        if average:
            res1.append(sum(list1) / len(list1))
            res2.append(sum(list2) / len(list2))
        else:
            res1.append(sum(list1))
            res2.append(sum(list2))

    path3 = file_path % 3
    file3 = pd.read_csv(path3)
    res3 = list(file3[column_name])
    res1 = sorted(res1)
    res2 = sorted(res2)
    res3 = sorted(res3)
    return res1, res2, res3, budget


if __name__ == '__main__':
    paint_rate("2", "rate", "Budget", "Task accomplishment ratio", "fig4a")
    paint_rate("2", "user_num", "Budget", "No. of selected users", "fig4b")
    paint_utility("2", "Budget", "Normalized utility value", "fig4c")
    paint_budget("2", "Budget", "Remaining budget", "fig4d")

    paint_rate("1", "rate", "Budget", "Task accomplishment ratio", "fig5a")
    paint_rate("1", "user_num", "Budget", "No. of selected users", "fig5b")
    paint_utility("1", "Budget", "Normalized utility value", "fig5c")
    paint_budget("1", "Budget", "Remaining budget", "fig5d")

    paint_line("rate", "Budget", "Task accomplishment ratio", True, "fig6a")
    paint_line("user_num", "Budget", "No. of selected users", False, "fig6b")
    paint_line("ac_utility", "Budget", "Total utility value", False, "fig6c")
    paint_bar("budget_save", "Budget", "Remaining budget", "fig6d")
