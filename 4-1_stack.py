# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 4-1_stack.py
@time: 2020/11/3 9:26
@description:使用Python的list列表实现栈这一数据结构
"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []  # 使用Python的list（顺序表）来充当栈的数据容器

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        # 为了时间复杂度最低，顺序表尾部操作时间复杂度最低
        # 使用什么样的数据容器，就要采用对应时间复杂度最低的操作来实现
        self.__list.append(item)  # 开口在尾部

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()  # 开口在尾部

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
