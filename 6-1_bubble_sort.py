# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-1_bubble_sort.py
@time: 2020/11/5 9:29
@description:
"""


def bubble_sort(a_list):
    """冒泡排序"""
    n = len(a_list)
    for j in range(n - 1):
        # 班长要走多少次
        count = 0
        for i in range(n - 1 - j):
            # 班长从头走到尾
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
