import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from scipy import interpolate
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

xFont = {'weight': 'bold', 'size': 12}

is_save = False


# node_id,t,budget,K,ep_utility,ac_utility

def paint_utility(name: str, x_label, y_label):
    res = []
    res2 = []
    round1 = [_ for _ in range(1, 13)]
    for i in range(0, 5):
        path = "result/%s.csv" % name
        file = pd.read_csv(path)
        file = file[(file['budget'] == 200 * 12) & (file['K'] == 15) & (file['node_id'] == i)]
        res2.append(list(file['ep_utility']))

    for r in res2:
        tmp = []
        for i in range(len(r)):
            tmp.append(sum(r[:i + 1]))
        res.append(tmp)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(round1, res[0], linewidth=2, marker='*', markersize=8, color='green', label="Node 1")
    plt.plot(round1, res[1], linewidth=2, marker='.', markersize=8, color='red', label='Node 2')
    plt.plot(round1, res[2], linewidth=2, marker='v', markersize=8, color='skyblue', label='Node 3')
    plt.plot(round1, res[3], linewidth=2, marker='x', markersize=8, color='blue', label='Node 4')
    plt.plot(round1, res[4], linewidth=2, marker='p', markersize=8, color='gray', label='Node 5')
    plt.legend(fontsize=10)  # 显示图例

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()


def paint_total_by_budget(x_label, y_label):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(1, 5):
        tmp = []
        for b in range(200, 801, 50):
            path = "result/result%d.csv" % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == b * 12) & (file['K'] == 9)]
            tmp.append(sum(list(file['ac_utility'])))
        res.append(tmp)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(budget, sorted(res[0]), linewidth=2, marker='*', color='green', label="EN-CMAB")
    plt.plot(budget, sorted(res[1]), linewidth=2, marker='.', color='red', label='ε-Frist')
    plt.plot(budget, sorted(res[2]), linewidth=2, marker='v', color='skyblue', label='Exploration')
    plt.plot(budget, sorted(res[3]), linewidth=2, marker='x', color='blue', label='Exploitation')

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel(x_label, xFont)
    plt.ylabel(y_label, xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()


def paint_total_by_users_num(budget):
    res = []
    user = [_ for _ in range(5, 16)]
    for i in range(1, 5):
        tmp = []
        for k in range(5, 16):
            path = "result/result%d.csv" % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == budget * 12) & (file['K'] == k)]
            tmp.append(sum(list(file['ac_utility'])))
        res.append(tmp)

    plt.figure(figsize=(4, 3.2), dpi=200)
    plt.plot(user, sorted(res[0]), linewidth=2, marker='*', color='green', label="EN-CMAB")
    plt.plot(user, sorted(res[1]), linewidth=2, marker='.', color='red', label='ε-Frist')
    plt.plot(user, sorted(res[2]), linewidth=2, marker='v', color='skyblue', label='Exploration')
    plt.plot(user, sorted(res[3]), linewidth=2, marker='x', color='blue', label='Exploitation')

    plt.legend(fontsize=10)  # 显示图例

    plt.xlabel("No. of users (Budget=%d)" % budget, xFont)
    plt.ylabel('Total utility value', xFont)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()


def pain3d(x_label, y_label, z_label):
    res = []
    user = [_ for _ in range(5, 16)]
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(1, 5):
        tmp = []
        for k in range(0, 11):
            path = "result/result%d.csv" % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == budget[k] * 12) & (file['K'] == user[k])]
            tmp.append(sum(list(file['ac_utility'])))
        res.append(tmp)
    plt.figure(figsize=(4.6, 4), dpi=200)
    ax = plt.axes(projection='3d')
    ax.plot3D(user, budget[:11], res[0], linewidth=2, marker='*', color='green', label="EN-CMAB")
    ax.plot3D(user, budget[:11], res[1], linewidth=2, marker='.', color='red', label='ε-Frist')
    ax.plot3D(user, budget[:11], res[2], linewidth=2, marker='v', color='skyblue', label='Exploration')
    ax.plot3D(user, budget[:11], res[3], linewidth=2, marker='x', color='blue', label='Exploitation')
    ax.legend(fontsize=11)  # 显示图例
    ax.set_xlabel(x_label, xFont)
    ax.set_ylabel(y_label, xFont)
    ax.set_zlabel(z_label, xFont)
    plt.show()


def paint3d():
    res = []
    user = [_ for _ in range(5, 16)]
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(1, 5):
        tmp = []
        for k in range(0, 11):
            path = "result/result%d.csv" % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == budget[k] * 12) & (file['K'] == user[k])]
            tmp.append(sum(list(file['ac_utility'])))
        res.append(tmp)
    plt.figure(figsize=(4.6, 4), dpi=200)
    Z = np.zeros(shape=(len(user), len(budget[:11])))
    for i in range(len(user)):
        for j in range(len(budget[:11])):
            pass


if __name__ == '__main__':
    # paint_utility('result1', 'No. of rounds (Budget=200, K=15)', 'Total utility value')
    # paint_total_by_budget('Budget (K=9)', 'Total utility value')
    # paint_total_by_users_num(200)
    # pain3d('No. of users', 'Budget', 'Total utility value')
    paint_total_by_users_num(800)

