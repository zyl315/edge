from code.bean import Node
from code.ENUR import ENUR as T1
from code.ENUR import BRD_ENUR as T2
from code.ENUR import QIM as T3
import copy

if __name__ == '__main__':
    T = 12
    B = 300
    for B in range(200, 801, 100):
        print(B)
        for i in range(10):
            print('\t%d' % i)
            res = Node.produce_task(T, B, num=100)
            res1 = copy.deepcopy(res)
            res2 = copy.deepcopy(res)

            print('ENUR')
            T1.init(res1, B)
            print('BRD_ENUR')
            T2.init(res2, B)

    for B in range(200, 201, 100):
        print('QIM')
        res3 = Node.produce_task2(T, B, num=100)
        T3.init(res3, B)
