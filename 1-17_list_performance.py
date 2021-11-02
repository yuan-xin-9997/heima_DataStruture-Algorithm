# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 1-17_list_performance.py
@time: 2020/9/30 15:23
@description:Python内置类型（list列表）性能分析，构建新列表的性能分析

结果分析：
append: 0.7037090999999998
+: 0.8283357999999996
[i for i in range(10000)]: 0.3342309000000001
list(range(10000)): 0.2023722000000001
extend: 1.0431327000000001
append: 0.6823193999999999
insert: 1.2023741000000001
--------------------------------------------------
list(range(10000))效率最高
insert效率最低
"""

from timeit import Timer


def t1():
    """
    测试Python列表的append操作的性能
    :return:
    """
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    """
    测试Python列表的+操作的性能
    :return:
    """
    li = []
    for i in range(10000):
        li += [i]


def t3():
    """
    测试Python列表的[]操作的性能
    :return:
    """
    li = [i for i in range(10000)]


def t4():
    """
    测试Python列表的操作的性能
    :return:
    """
    li = list(range(10000))


def t5():
    """
    测试Python列表的extend操作的性能
    :return:
    """
    li = []
    for i in range(10000):
        li.extend([i])


def t6():
    li = []
    for i in range(10000):
        li.append(i)


def t7():
    li = []
    for i in range(10000):
        li.insert(i, i)


timer1 = Timer("t1()", "from __main__ import t1")
print('append:', timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print('+:', timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print('[i for i in range(10000)]:', timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print('list(range(10000)):', timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print('extend:', timer5.timeit(1000))

timer6 = Timer("t6()", "from __main__ import t6")
print('append:', timer6.timeit(1000))

timer7 = Timer("t7()", "from __main__ import t7")
print('insert:', timer7.timeit(1000))

print('-' * 50)
