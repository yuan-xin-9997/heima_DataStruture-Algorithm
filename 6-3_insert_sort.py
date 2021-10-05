# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-3_insert_sort.py
@time: 2020/11/9 20:00
@description:
"""


def insert_sort(a_list):
    """插入排序"""
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, len(a_list)):
        # j = [1,2,3,...,n-1]
        i = j   # i 代表内存循环起始值
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if a_list[i] < a_list[i-1]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
