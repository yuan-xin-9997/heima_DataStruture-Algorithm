# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-2_select_sort.py
@time: 2020/11/6 9:17
@description:
"""


def select_sort(a_list):
    """选择排序"""
    n = len(a_list)
    for j in range(n-1):
        min_index = j
        for i in range(j + 1, n):
            if a_list[min_index] > a_list[i]:
                min_index = i
        a_list[j], a_list[min_index] = a_list[min_index], a_list[j]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
