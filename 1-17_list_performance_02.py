# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 1-17_list_performance_02.py
@time: 2021/11/2 20:09
@description:
来自上交所技术-2022校招-应用开发工程师
在Python3中，实现新列表扩展原有列表功能时，例如，当a=[1,2,3], b=[4,5,6]时,要想使a=[1,2,3,4,5,6].则下列方法中正确但效率最低的是()。
A a[len(a):]=b
B a.extend(b)
C a = a+b
D a.append(b)

分析：
D的结果为[1, 2, 3, [4, 5, 6]]，是错的
A这种赋值方式也是可行的

结果分析：
a[len(a):] = b: 0.0023941000000000656
a.extend(b): 0.0020889999999997855
c = a + b: 1.3032008999999998
--------------------------------------------------
+这种方式效率最低
"""

from timeit import Timer

a = [1, 2, 3]
b = [4, 5, 6]


def t1():
    a[len(a):] = b
    return a


def t2():
    a.extend(b)
    return a


def t3():
    c = a + b
    return c


timer1 = Timer("t1()", "from __main__ import t1")
print('a[len(a):] = b:', timer1.timeit(10000))

timer2 = Timer("t2()", "from __main__ import t2")
print('a.extend(b):', timer2.timeit(10000))

timer3 = Timer("t3()", "from __main__ import t3")
print('c = a + b:', timer3.timeit(10000))

print('-' * 50)
