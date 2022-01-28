# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 6-3_insert_sort.py
@time: 2020/11/9 20:00
@description:
"""
import logging
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')

import os
logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
logging.debug('this is a message')

# -*-coding:utf-8-*-

import logging


def console_out(logFilename):
    ''''' Output log to file and console '''
    # Define a Handler and set a format which output to file
    logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename=logFilename,  # log文件名
        filemode='w')  # 写入模式“w”或“a”
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)  # 实例化添加handler

    # Print information              # 输出日志级别
    logging.debug('logger debug message')
    logging.info('logger info message')
    logging.warning('logger warning message')
    logging.error('logger error message')
    logging.critical('logger critical message')


if __name__ == "__main__":
    console_out('logging.log')

def insert_sort(a_list):
    """
    插入排序
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从
    后向前扫描，找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空
    间。
    最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
    最坏时间复杂度：O(n2)
    稳定性：稳定
    """
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, len(a_list)):
        # j = [1,2,3,...,n-1]
        i = j   # i 代表内层循环起始值
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if a_list[i-1] > a_list[i]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    console_out('logging.log')
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
