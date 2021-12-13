import math
import random

from code.bean import User, Task
from code.util import util_csv

EARTH_REDIUS = 6378.137


class Node:
    def __init__(self, _id, position):
        self.id = _id
        self.position = position
        self.budget = 0
        # 结点划分的兴趣点
        self.points = []
        # 结点划分的参与者
        self.m_all = []
        # 候选参与者
        self.m_candidate = []
        # 被选择的参与者
        self.m_select = []
        # 上一轮被选择的参与者
        self.m_last_select = []
        # 离开的参与者
        self.m_departure = []
        # 阈值
        self.threshold = 0
        # 实际完成的兴趣点
        self.actual_points = {}
        # 未完成的兴趣点
        self.unfinished_points = []
        # 总效用值
        self.utility = []

    # 分配预算
    def division_budget(self, task):
        self.budget = task.budget * (len(self.points) / len(task.points))


# 划分兴趣点
def division_points(task, nodes):
    for p in task.points:
        d = float('inf')
        _id = 0
        for i in range(len(nodes)):
            tmp_d = getDistance(nodes[i].position[0], nodes[i].position[1], p.position[0], p.position[1])
            if tmp_d < d:
                d = tmp_d
                _id = i
        nodes[_id].points.append(p)
        nodes[_id].unfinished_points.append(p)

    for n in nodes:
        n.m_candidate = n.m_all.copy()
        n.division_budget(task)


# 划分参与者
def division_user(users, nodes, divide=1):
    tmp_users = users.copy()
    for i in range(len(users)):
        m = tmp_users[random.randint(0, len(tmp_users) - 1)]

        index = i % len(nodes)
        nodes[index].m_all.append(m)

        sample = random.sample(nodes[index].points, len(nodes[index].points) // divide)
        m.interest_points = sample.copy()
        m.unfinished_points = sample.copy()

        tmp_users.remove(m)


# 计算地球距离
def rad(d):
    return d * math.pi / 180.0


def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    return s


def produce_task(T, B, num, deep=5, divide=1):
    row_points = util_csv.read_csv('Point')
    row_node = util_csv.read_csv('Node')
    row_user = util_csv.read_csv('User')
    points = []
    nodes = []
    users = []
    # 产生兴趣点
    for p in row_points[:num]:
        point = Task.Point(p[0], p[1], p[2], deep)
        points.append(point)
    task = Task.Task(T, B, points)
    # 产生边缘节点
    for n in row_node:
        node = Node(n[0], (n[1], n[2]))
        nodes.append(node)
    division_points(task=task, nodes=nodes)

    # 产生参与者
    for u in row_user[:]:
        user = User.User(u[0], u[1], u[2], position=(u[3], u[4]), credit=u[5])
        users.append(user)
    division_user(users, nodes, divide)

    return [task, nodes]


def produce_task2(T, B, num):
    row_points = util_csv.read_csv('Point')
    row_user = util_csv.read_csv('User')
    points = []
    nodes = []
    users = []

    # 产生兴趣点
    for p in row_points[:]:
        point = Task.Point(p[0], p[1], p[2], 5)
        points.append(point)
    task = Task.Task(T, B, points)
    # 产生边缘节点
    node = Node(6, (0, 0))
    node.points = points.copy()
    node.budget = B

    # 产生参与者
    for u in row_user[:num]:
        user = User.User(u[0], u[1], u[2], position=(u[3], u[4]), credit=u[5])
        tmp_points = random.sample(points, 40)
        user.interest_points = tmp_points.copy()
        user.unfinished_points = tmp_points.copy()
        users.append(user)
    node.m_all = users.copy()

    nodes.append(node)
    return [task, nodes]
