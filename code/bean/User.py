# 参与者类
class User:
    def __init__(self, _id, trip_second, fare, position, credit):
        self.id = _id
        self.trip_second = trip_second
        self.credit = credit
        # 参与者要求感知任务的报酬
        self.reward = fare
        # 参与者额外奖励
        self.extra = 0
        # 参与者位置
        self.position = position
        # 参与者感知的兴趣点集合
        self.interest_points = []
        # 参与者实际完成的兴趣点
        self.actual_points = []
        # 参与者实际完成的兴趣点集合
        self.actual_points_p = []
        # 参与者未完成的兴趣点
        self.unfinished_points = []
        # 兴趣点数据
        self.point_data = {}
        # 到达时间
        self.arrive_time = 0
        # 离开时间
        self.departure_time = 0
        # 兴趣点数据质量
        self.data_quality = []
        # 参与者被选择的次数
        self.count = 1
        # 参与者执行任务能力
        self.ability = self.credit


# 参与位置
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
