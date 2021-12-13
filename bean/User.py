import pymysql
import uuid as uid
import random

# 连接数据库
db = pymysql.connect("localhost", "root", "root", "crowdsensing", charset='utf8')


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


# 从数据库中获取所有历史参与者信息
def get_all_user():
    users = []
    sql = "select * from user "
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            users.append(User(result[0], result[1], result[2]))
    except:
        print("error:unable to fetch data")

    return users


# 关闭数据库连接
def db_close():
    db.close()


# 往数据库添加参与者
def insert_user(user):
    sql = "insert into user(uuid,credit) value('%s', %s)" % (user.uuid, user.credit)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except AttributeError:
        db.rowback()
        print("error: insert user fail")


# 更新用户信息
def update_user(uuid, credit):
    sql = "update user set credit = %s where uuid = '%s'" % (credit, uuid)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("error: update user fail")


# 模拟新的用户到达,并且初始化信誉值为0.5
def add_new_user():
    _uuid = uid.uuid1().hex
    user = User(None, _uuid, credit=0.5)
    insert_user(user)
    return user


# 产生感知任务参与者的候选集
def generate_candidate(num):
    # 从数据库获得所有的历史参与者
    user_from_database = get_all_user()
    num = min(num, len(user_from_database))
    m_candidate = random.sample(user_from_database, num)

    for u in m_candidate:
        # 模拟参与者提出感知的报酬,随机给出
        u.reward = random.randint(2, 10)
        # 模拟参与者出现的随机位置
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        u.position = (x, y)

    return m_candidate


def generate_candidate2(num, point, x_max, y_max, pb=0.1):
    m_candidate = []
    # 从数据库获得所有的历史参与者
    user_from_database = get_all_user()

    for i in range(num):

        if len(user_from_database) == 0:
            break
        u = user_from_database[i]
        user_from_database.remove(u)
        # 模拟参与者请求的感知兴趣点集合，随机选择

        num = random.randint(1, 30)
        u.interest_points = random.sample(point, num)
        u.unfinished_points = u.interest_points.copy()

        # 模拟参与者提出感知的报酬,随机给出
        u.reward = random.randint(2, 10)

        # 模拟参与者随机位置
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        u.position = (x, y)
        m_candidate.append(u)

    return m_candidate


if __name__ == '__main__':
    pass
