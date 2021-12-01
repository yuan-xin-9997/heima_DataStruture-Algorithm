# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-4_quick_sort.py
@time: 2020/11/13 19:29
@description:
"""


def quick_sort(a_list, first, last):
    """
    快速排序
    快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），通过一趟排序将要排序的数据分割成独立的两部分，
    其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
    以此达到整个数据变成有序序列。
    步骤为：
        1.从数列中挑出一个元素，称为"基准"（pivot），
        2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
        在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
        3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会结束，因为在每次的
    迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    """
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

        # low 游标 右移
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
