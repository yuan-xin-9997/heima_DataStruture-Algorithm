# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 5-2_double_queue.py
@time: 2020/11/4 9:34
@description:
"""


class Deque(object):
    """双端队列"""

    def __init__(self):
        # 使用Python顺序表List来充当数据容器
        self.__list = []

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def add_front(self, item):
        """在对头添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """在对尾添加元素"""
        self.__list.append(item)

    def remove_front(self):
        """在对头删除元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """在对尾删除元素"""
        return self.__list.pop()

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
