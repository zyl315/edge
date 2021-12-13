from code.bean import Node
import random
import numpy as np
import math

# 边缘节点集合
nodes = []
# 每个兴趣点感知次数
deep = 5
# 感知预算B
B = 800
# 感知时间T
T = 12

task = None


def init(res, budget, k):
    global task, nodes, B
    B = budget
    K = k

    task = res[0]
    nodes = res[1]
    for n in res[1]:
        print('id=%d' % n.id, len(n.points), len(n.m_all))
    online_quality_aware(T, K)


def online_quality_aware(time, K):
    t = 1
    while t <= time:
        print('t=%d' % t)
        for n in nodes:
            if n.id == 1:
                break
            n.m_select.clear()
            candidate = n.m_all.copy()

            # 进行用户的能力更新
            for m in candidate:
                q = math.sqrt(T * np.log(t) / m.count)
                ability = m.credit + 0.1 * ((1 / np.pi) * np.arctan(q) + 0.5)
                m.ability = min(1, ability)

            while len(n.m_select) <= K:
                # 选出边际效应最大的参与者
                m = argmax(candidate, n.m_select, n)
                if n.budget - m.reward < 0:
                    print("\t budget run out of")
                    break
                n.budget -= m.reward
                n.m_select.append(m)
                m.actual_points.clear()
                m.count += 1
                candidate.remove(m)
                print(
                    "\t node %d, user %3d is selected %3d times, his ability is %.3f,"
                    " credit is %.3f  and reward is %.3f"
                    % (n.id, m.id, m.count - 1, m.ability, m.credit, m.reward))

            # 模拟执行任务
            ep_utility = utility_function(n.m_select, n)
            ac_utility = run_task(n.m_select, t, n)
            n.utility.append((ep_utility, ac_utility))
            print("\t node id=%d ep_utility=%d ac_utility=%d" % (n.id, ep_utility, ac_utility))
            print()
        t += 1
        # print(list(map(lambda m: m.ability, nodes[0].m_all)))


# 模拟被选择的参与者执行任务
def run_task(m_selected, t, node):
    av_ability = node_average_ability(node)
    av_credit = node_average_credit(node)

    for m in m_selected:
        for p in m.interest_points:
            # 按顺序选择兴趣点,随机模拟完成
            ran = random.random()

            if ran < m.ability:
                m.actual_points.append(p.id)
                # 边缘节点记录完成的兴趣点
                m.position = (p.x, p.y)
                # m.unfinished_points.remove(p)

    return actual_utility(m_selected, node)


def argmax(candidate, m_selected, node):
    m_max = 0
    value = 0
    for i in range(len(candidate)):
        v = (utility_function(m_selected + [candidate[i]], node) - utility_function(m_selected, node)) / candidate[
            i].reward
        if v > value:
            value = v
            m_max = i
    return candidate[m_max]


# 计算边际效用函数
def utility_function(M, node: Node):
    ans = 0
    for p in node.points:
        e_p = 0
        for m in M:
            e_p += 1 * m.ability
        ans += min(p.data, e_p)
        # ans += e_p
    return ans


# 实际效用函数
def actual_utility(M, node: Node):
    ans = 0
    for p in node.points:
        e_p = 0
        for m in M:
            if p.id in m.actual_points:
                e_p += 1
        ans += min(p.data, e_p)
        # ans += e_p
    return ans


# 计算边缘节点的平均信誉
def node_average_credit(node: Node):
    tmp = 0
    for m in node.m_all:
        tmp += m.credit
    average_credit = tmp / len(node.m_all)
    return average_credit


# 计算边缘节点的平均能力
def node_average_ability(node: Node):
    tmp = sum(map(lambda m: m.ability, node.m_all))
    return tmp / len(node.m_all)


if __name__ == '__main__':
    T = 12
    B = 200 * T
    res = Node.produce_task(T, B, num=100, deep=5, divide=2)
    init(res, B, k=5)
