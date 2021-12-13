import random


# 任务类
class Task:
    # 初始化一个任务
    def __init__(self, time, budget, points):
        # 任务时间
        self.time = time
        # 感知预算
        self.budget = budget
        # 保留预算
        self.save_budget = 0
        # 兴趣点集合
        self.points = points
        # 实际完成的数据点情况
        self.actual_points = [0 for _ in range(len(points))]
        # 总数据量
        self.data = calculate_data(points)


# 兴趣点类
class Point:
    # 初始化一个兴趣点
    def __init__(self, _id, x, y, data):
        self.id = _id
        # 坐标x
        self.x = x
        # 坐标y
        self.y = y
        self.position = (x, y)
        # 单个兴趣点要收集的数据量
        self.data = data
        # 该点平均数据质量
        self.average_quality = 0


# 计算需要收集的数据总量
def calculate_data(points):
    all_data = 0
    for point in points:
        all_data += point.data
    return all_data


# 产生兴趣点集合
def generate_points(num, x_max, y_max, data_max):
    points = []
    for i in range(num):
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        data = random.randint(1, data_max)
        point = Point(i, x, y, data)
        points.append(point)
    return points


if __name__ == '__main__':
    point_list = generate_points(100, 100, 100, 3)
