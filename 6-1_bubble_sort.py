# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-1_bubble_sort.py
@time: 2020/11/5 9:29
@description:
"""


def bubble_sort(a_list):
    """
    冒泡排序
    冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，
    如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
    冒泡排序算法的运作如下：
        比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        针对所有的元素重复以上的步骤，除了最后一个。
        持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束）
    最坏时间复杂度：O(n2)
    稳定性：稳定
    """
    n = len(a_list)
    for j in range(n - 1):
        # 班长要走多少次
        count = 0
        for i in range(n - 1 - j):
            # 班长从头走到尾
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
