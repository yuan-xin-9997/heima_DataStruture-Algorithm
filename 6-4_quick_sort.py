# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-4_quick_sort.py
@time: 2020/11/13 19:29
@description:
"""


def quick_sort(a_list, first, last):
    """快速排序"""
    # 判断列表是否只有一个元素，如果有，则返回
    if first >= last:
        return

    mid_value = a_list[first]
    low = first
    high = last

    while low < high:
        # high 游标 左移
        while low < high and a_list[high] >= mid_value:
            high -= 1
        a_list[low] = a_list[high]

        # low游标 右移
        while low < high and a_list[low] < mid_value:
            low += 1
        a_list[high] = a_list[low]
    # 从循环退出时，low==high
    a_list[low] = mid_value

    # 对low/high左边的列表执行快速排序（递归）
    quick_sort(a_list, first, low-1)

    # 对low/high右边的列表执行快速排序（递归）
    quick_sort(a_list, high+1, last)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
