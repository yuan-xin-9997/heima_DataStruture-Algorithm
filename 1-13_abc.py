# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 1-13_abc.py
@time: 2020/9/30 11:37
@description:用来展示算法设计差异导致运行时间的差异

# 如果 a+b+c=N且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# a、b依次遍历，c的值由a、b来确定
# a
# b
# c=1000-a-b

"""


import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            print('a={},b={},c={}'.format(a, b, c))
end_time = time.time()
print('time:{}'.format(end_time-start_time))
