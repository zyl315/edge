from bean import Node
import random
import numpy as np
import math
from sklearn.cluster import KMeans

# 边缘节点集合
nodes = []
# 每个兴趣点感知次数
deep = 5
# 感知预算B
B = 800
# 感知时间T
T = 12
# 单位间隔
slot = 60

task = None


def init(res, budget):
    global task, nodes, B
    task = res[0]
    nodes = res[1]
    B = budget
    online_quality_aware(T)


def online_quality_aware(time):
    t = 1
    for n in nodes:
        n.threshold = len(n.points) * deep / n.budget
    while t <= time:
        for n in nodes:
            if t == 1:
                candidate = n.m_all.copy()
                while len(candidate) != 0:
                    # 选出边际效应最大的参与者
                    m = argmax(candidate, n.m_select, n)
                    threshold = (utility_function(n.m_select + [m], n) - utility_function(n.m_select, n)) / m.reward

                    if threshold >= n.threshold and n.budget > m.reward:
                        n.m_select.append(m)
                        n.budget -= m.reward
                        n.m_all.remove(m)
                        m.arrive_time = t
                    candidate.remove(m)

            m_departure = run_task(n.m_select, t, n)
            n.m_departure.extend(m_departure)
            # threshold_update(m_departure, n)

            rate = node_task_complete(n)

            if t == time:
                ep_utility = utility_function(n.m_departure, n)
                ac_utility = actual_utility(n.m_departure, n)
                print(
                    '\t node_id=%d rate=%f budget=%f points_num=%d remain=%d all_user_num=%d ep_utility=%f '
                    'ac_utility=%f' % (
                        n.id, rate, n.budget, len(n.points), len(n.m_select), len(n.m_departure), ep_utility,
                        ac_utility))

                # csv.write_csv(('result2_%d' % n.id),
                #               [int(n.id), rate, n.budget, len(n.m_departure), task.budget, ep_utility, ac_utility])

        budget_update()
        t += 1

    # for n in nodes:
    #     quality_estimation(n)
    #     rewards_distribution(n)


# 模拟被选择的参与者执行任务
def run_task(m_selected, t, node):
    m_departure = list()
    if t == T:
        m_departure.extend(m_selected)
    for m in m_selected:
        # 用户已完成全部兴趣点的感知，用户离开
        if len(m.unfinished_points) == 0:
            m.departure_time = t
            node.m_departure.append(m)
            break
        # 用户感知任务停留时间超过当前任务时间则认为用户离开
        if m.trip_second >= (t - m.arrive_time) * slot:
            count = random.randint(1, int(len(node.points) / T + 0.5))
            count = min(count, len(m.unfinished_points))
            for i in range(count):
                # 每次随机选取一个随机兴趣点,随机模拟是否完成
                index = random.randint(0, len(m.unfinished_points) - 1)
                p = m.unfinished_points[index]
                # 完成该兴趣点
                ran = random.random()
                # 完成该兴趣点
                if ran <= m.credit:
                    m.actual_points.append(p.id)
                    m.actual_points_p.append(p)

                    m.point_data[p.id] = random.random()
                    if p.id not in node.actual_points:
                        node.actual_points[p.id] = []
                    node.actual_points[p.id].append(m.id)

                m.position = (p.x, p.y)
                m.unfinished_points.remove(p)

        else:
            # 添加到任务离开者结合
            m.departure_time = t
            m_departure.append(m)
            # 模拟用户中途离开任务
    for m in m_departure:
        if m in m_selected:
            m_selected.remove(m)
    return m_departure


# 阈值和预算更新函数
def threshold_update(m_departure, node):
    if len(m_departure) == 0:
        return
    all_reward = 0
    for m in m_departure:
        all_reward += m.reward
    delta = (actual_utility(m_departure, node) - utility_function(m_departure, node)) / (all_reward + 0.00000001)
    new_threshold = (1.1 ** delta) * (len(node.points) * deep - actual_utility(node.m_departure, node)) / node.budget
    node.threshold = new_threshold


def budget_update():
    un_ratio_list = []
    all_budget = 0
    # 预算回收
    for n in nodes:
        all_budget += n.budget
        n.budget = 0
        tmp_rate = node_task_complete(n)
        un_ratio_list.append(1 - tmp_rate)

    # 预算再分配
    for i in range(len(nodes)):
        nodes[i].budget = all_budget * (un_ratio_list[i] / sum(un_ratio_list))


def argmax(candidate, m_selected, node):
    m_max = 0
    value = 0
    for i in range(len(candidate)):
        v = utility_function(m_selected + [candidate[i]], node) \
            - utility_function(m_selected, node)
        if v > value:
            value = v
            m_max = i
    return candidate[m_max]


# 计算边际效用函数
def utility_function(M, node: Node):
    ans = 0
    average_credit = node_average_credit(node)
    for p in node.points:
        e_p = 0
        for m in M:
            if m.credit >= average_credit:
                e_p += 1 * np.sin(np.pi * 0.5 * m.credit) * 1
            else:
                e_p += 1 * np.sin(np.pi * 0.5 * m.credit) * 0.8
        ans += min(p.data, e_p)
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
    return ans


# 计算边缘节点的平均信誉
def node_average_credit(node: Node):
    average_credit = 0
    tmp = 0
    for m in node.m_all:
        tmp += m.credit
    average_credit = tmp / len(node.m_all + node.m_departure + node.m_select)
    return average_credit


# 计算边缘节点任务完成度
def node_task_complete(node: Node):
    all_user = node.m_departure + node.m_select
    actual_data = [0 for _ in range(len(node.points))]
    request_data = [deep for _ in range(len(node.points))]
    m_dict = {}
    for m in all_user:
        for i in m.actual_points:
            if i not in m_dict:
                m_dict[i] = 1
            if m_dict[i] < deep:
                m_dict[i] += 1
    actual_data = list(m_dict.values()) + [0] * (len(node.points) - len(m_dict))
    rate = 1 - cal_F(np.array(request_data) - np.array(actual_data)) / cal_F(request_data)
    return rate


# F范数
def cal_F(A):
    ans = 0
    for i in A:
        ans += i ** 2
    return np.sqrt(ans)


# 数据质量评估函数
def quality_estimation(node: nodes):
    for p in node.points:
        X = []
        user = []
        user_dist = []
        for m in node.m_departure:
            if p.id in m.point_data:
                X.append((m.id, m.point_data[p.id]))
                user.append(m)
        if len(X) == 0:
            break
        kmeans = KMeans(n_clusters=1, random_state=0).fit(np.array(X))
        cluster_center = kmeans.cluster_centers_[0]

        all_dist = 0
        tao = 0.0000001
        for x in X:
            dist = math.sqrt((x[1] - cluster_center[1]) ** 2)
            user_dist.append(dist + tao)
            all_dist += dist

        all_dist_q = 0
        for i in range(len(user_dist)):
            all_dist_q += (1 / (user_dist[i] / (all_dist + tao)))

        tmp_data_quality = 0
        for i in range(len(user_dist)):
            data_quality = (1 / (user_dist[i] / (all_dist + tao))) / (all_dist_q + tao)
            tmp_data_quality += data_quality
            user[i].data_quality.append(data_quality)

        p.average_quality = tmp_data_quality / len(user_dist)

    for m in node.m_departure:
        d_q = sum(m.data_quality)
        tmp_average = 0
        for p in m.actual_points_p:
            tmp_average += p.average_quality
        final_quality = d_q - tmp_average
        new_credit = m.credit + 1 * 1 / (1 + np.e ** (1 - final_quality))


# 最终奖励分配
def rewards_distribution(node: nodes):
    total_credit = 0
    for m in node.m_departure:
        total_credit += m.credit

    for m in node.m_departure:
        m.extra_reward = node.budget * (m.credit / total_credit)


if __name__ == '__main__':
    T = 12
    for B in range(200, 801, 50):
        print("budget=%d" % B)
        res = Node.produce_task(T, B, num=100)
        init(res, B)
        print()
