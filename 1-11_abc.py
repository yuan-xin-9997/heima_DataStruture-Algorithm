# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 1-11_abc.py
@time: 2020/9/30 10:51
@description:用来展示算法设计差异导致运行时间的差异

# 如果 a+b+c=N且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# a、b、c依次遍历
# a
# b
# c

"""


import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print('a={},b={},c={}'.format(a, b, c))
end_time = time.time()
print('time:{}'.format(end_time-start_time))
