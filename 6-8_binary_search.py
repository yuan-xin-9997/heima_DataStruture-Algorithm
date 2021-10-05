# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-8_binary_search.py
@time: 2020/11/17 20:32
@description:
"""


def binary_search(a_list, item):
    """二分查找（递归实现）"""
    n = len(a_list)
    if n > 0:
        mid = n // 2
        if a_list[mid] == item:
            return True
        elif item < a_list[mid]:
            return binary_search(a_list[:mid], item)
        else:
            return binary_search(a_list[mid+1:], item)
    else:
        return False


def binary_search_2(a_list, item):
    """二分查找（非递归实现）"""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if a_list[mid] == item:
            return True
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 100))
    print(binary_search(li, 54))

    status = binary_search_2(li, 100)
    print(status)
    print(binary_search_2(li, 54))
