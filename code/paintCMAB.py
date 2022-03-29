import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

xFont = {'weight': 'bold', 'size': 12}
dpi = 200
figsize = (4, 3.2)
fontsize = 12
linewidth = 2
file_path = "../data/URMB/result%d.csv"
save_path = "../results/fig2/%s.png"


def paint_utility(name, budget, user_num, save_name):
    res = []
    res2 = []
    round1 = [_ for _ in range(1, 13)]
    for i in range(0, 5):
        path = file_path % name
        file = pd.read_csv(path)
        file = file[(file['budget'] == budget * 12) & (file['K'] == user_num) & (file['node_id'] == i)]
        res2.append(list(file['ep_utility']))

    for r in res2:
        tmp = []
        for i in range(len(r)):
            tmp.append(sum(r[:i + 1]))
        res.append(tmp)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(round1, res[0], linewidth=linewidth, marker='*', markersize=8, color='green', label="Node 1")
    plt.plot(round1, res[1], linewidth=linewidth, marker='.', markersize=8, color='red', label='Node 2')
    plt.plot(round1, res[2], linewidth=linewidth, marker='v', markersize=8, color='skyblue', label='Node 3')
    plt.plot(round1, res[3], linewidth=linewidth, marker='x', markersize=8, color='blue', label='Node 4')
    plt.plot(round1, res[4], linewidth=linewidth, marker='p', markersize=8, color='gray', label='Node 5')
    plt.legend(fontsize=fontsize - 2)

    plt.xlabel('No. of rounds (Budget=%d, K=%d)' % (budget, user_num), xFont)
    plt.ylabel('Total utility value', xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path % save_name)
    plt.show()


def paint_total_by_budget(user_num, save_name):
    res = []
    budget = [_ for _ in range(200, 801, 50)]
    for i in range(1, 5):
        tmp = []
        for b in range(200, 801, 50):
            path = file_path % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == b * 12) & (file['K'] == user_num)]
            tmp.append(sum(list(file['ac_utility'])))
        # tmp = sorted(tmp)
        res.append(tmp)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(budget, res[0], linewidth=linewidth, marker='*', color='green', label="EN-UMBR")
    plt.plot(budget, res[1], linewidth=linewidth, marker='.', color='red', label='ε-First')
    plt.plot(budget, res[2], linewidth=linewidth, marker='v', color='skyblue', label='Exploration')
    plt.plot(budget, res[3], linewidth=linewidth, marker='x', color='blue', label='Exploitation')

    plt.legend(fontsize=fontsize - 2)

    plt.xlabel("Budget (K=%d)" % user_num, xFont)
    plt.ylabel('Total utility value', xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path % save_name)
    plt.show()


def paint_total_by_users_num(budget, save_name):
    res = []
    user = [_ for _ in range(5, 16)]
    for i in range(1, 5):
        tmp = []
        for k in range(5, 16):
            path = file_path % i
            file = pd.read_csv(path)
            file = file[(file['budget'] == budget * 12) & (file['K'] == k)]
            tmp.append(sum(list(file['ac_utility'])))
        # tmp = sorted(tmp)
        res.append(tmp)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(user, res[0], linewidth=linewidth, marker='*', color='green', label="EN-UMBR")
    plt.plot(user, res[1], linewidth=linewidth, marker='.', color='red', label='ε-First')
    plt.plot(user, res[2], linewidth=linewidth, marker='v', color='skyblue', label='Exploration')
    plt.plot(user, res[3], linewidth=linewidth, marker='x', color='blue', label='Exploitation')

    plt.legend(fontsize=fontsize - 2)

    plt.xlabel("No. of users (Budget=%d)" % budget, xFont)
    plt.ylabel('Total utility value', xFont)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path % save_name)
    plt.show()


if __name__ == '__main__':
    # paint_utility(1, 200, 15, "fig7a0")
    # paint_utility(1, 300, 15, "fig7a1")
    # paint_utility(1, 600, 15, "fig7a2")

    # paint_utility(1, 300, 5, "fig7b0")
    # paint_utility(1, 300, 11, "fig7b1")
    # paint_utility(1, 300, 14, "fig7b2")

    paint_total_by_budget(7, "fig7c0")
    paint_total_by_budget(10, "fig7c1")
    paint_total_by_budget(13, "fig7c2")

    # paint_total_by_users_num(200, "fig8d0")
    # paint_total_by_users_num(300, "fig8d1")
    # paint_total_by_users_num(600, "fig8d2")
