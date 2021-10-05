# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-5_shell_sort.py
@time: 2020/11/10 9:21
@description:
"""


def shell_sort(a_list):
    """希尔排序"""
    gap = len(a_list) // 2
    while gap >= 1:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, len(a_list)):
            i = j
            while i > 0:
                if a_list[i] < a_list[i-gap]:
                    a_list[i], a_list[i-gap] = a_list[i-gap], a_list[i]
                    i -= gap
                else:
                    break
        # 缩短gap的步长
        gap //= 2


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
