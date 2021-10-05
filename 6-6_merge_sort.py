# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-6_merge_sort.py
@time: 2020/11/15 19:30
@description:
"""


def merge_sort(a_list):
    """归并排序"""

    n = len(a_list)

    if n <= 1:  # 递归停止条件
        return a_list

    mid = n // 2

    # left 表示 采用归并排序后形成的有序的新的列表（递归）
    left_li = merge_sort(a_list[:mid])

    # right 表示 采用归并排序后形成的有序的新的列表（递归）
    right_li = merge_sort(a_list[mid:])

    # 将两个有序的子序列left和right合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        elif left_li[left_pointer] > right_li[right_pointer]:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    li = merge_sort(li)
    print(li)
