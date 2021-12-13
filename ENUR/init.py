from bean import Node
from ENUR import RunTask as T0

if __name__ == '__main__':
    T = 12
    B = 300
    # for B in range(200, 801, 100):
    #     print(B)
    #     for i in range(10):
    #         print('\t%d' % i)
    #         res = Node.produce_task(T, B, num=100)
    #         res1 = copy.deepcopy(res)
    #         res2 = copy.deepcopy(res)
    #
    #         print('算法1')
    #         T1.init(res1, B)
    #         print('算法2')
    #         T2.init(res2, B)

    # for B in range(200, 201, 100):
    #     print('算法3')
    #     res3 = Node.produce_task2(T, B, num=100)
    #     T3.init(res3, B)

    res = Node.produce_task(T, B, num=100)
    T0.init(res, B)
