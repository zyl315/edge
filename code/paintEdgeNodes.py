import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
xFont = {'weight': 'bold', 'size': 12}

is_save = True
dpi = 400
figsize = (4, 3.2)
fontsize = 12
linewidth = 1.5
file_path = "../data/ENUR/result%s.csv"
save_path = "../results/fig/%s.png"

brd = [
    [34.80, 30.12, 30.79, 29.57, 29.83, 24.41, 23.18, 21.74, 0.40, 11.24, 3.71, 6.17],
    [56.25, 29.41, 29.63, 29.30, 30.69, 26.36, 22.97, 22.73, 14.46, 14.03, 1.42, 7.90],
    [26.40, 31.14, 30.89, 29.46, 28.80, 23.26, 21.82, 15.27, 11.04, 10.43, 9.39, 2.08],
    [22.95, 30.51, 26.97, 25.63, 24.77, 16.23, 20.06, 7.80, 14.9, 09.74, 7.93, 5.28],
    [12.15, 31.34, 22.94, 27.28, 27.13, 23.11, 18.01, 16.24, 15.88, 2.74, 7.98, 4.75]
]


def paint_rate(name: str, column_name: str, x_label, y_label, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(0, 5):
        path = "../data/ENUR/result%s.csv" % name
        file = pd.read_csv(path)
        file = file['node_id'] == i
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
    plt.tight_layout()
    if is_save:
        plt.savefig(save_path % save_name, dpi=dpi)
    plt.show()


def paint_budget_change(name: str, column_name: str, x_label, y_label, save_name):
    # res = brd
    res = []
    T = [_ for _ in range(1, 13)]
    if name == "1":
        res = brd
    else:
        for i in range(0, 5):
            path = "../results/ENUR/budget_change_%s.csv" % name
            file = pd.read_csv(path)
            file = file[file['node_id'] == i]
            res.append(list(file[column_name]))

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(T, res[0], linewidth=linewidth, marker='*', color='green', label="Node 1")
    plt.plot(T, res[1], linewidth=linewidth, marker='.', color='red', label='Node 2')
    plt.plot(T, res[2], linewidth=linewidth, marker='v', color='skyblue', label='Node 3')
    plt.plot(T, res[3], linewidth=linewidth, marker='x', color='blue', label='Node 4')
    plt.plot(T, res[4], linewidth=linewidth, marker='p', color='gray', label='Node 5')
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


if __name__ == '__main__':
    # paint_rate("1", "rate", "Budget", "BRD-ENUR\n Task accomplishment ratio", "fig8a")
    # paint_rate("4", "rate", "Budget", "QIM-EDGE\n Task accomplishment ratio", "fig8b")
    paint_budget_change("1", "budget_save", "Round T (B=300)", "BRD-ENUR budget variation", "fig9a")
    paint_budget_change("4", "budget_save", "Round T (B=300)", "QIM-EDGE budget variation", "fig9b")
