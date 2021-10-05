# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 3-3_double_link_list.py
@time: 2020/10/26 9:35
@description:
"""


class Node(object):
    """双链表的结点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
        # _prev是上一个节点的标识
        self.prev = None


class DoubleLinkList(object):
    """单链表实现（单链表的操作）：
        is_empty() 链表是否为空
        length() 链表长度
        travel() 遍历整个链表
        add(item) 链表头部添加元素
        append(item) 链表尾部添加元素
        insert(pos, item) 指定位置添加元素
        remove(item) 删除节点
        search(item) 查找节点是否存在
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=',')
            cur = cur.next
        print()

    def add(self, item):
        """头部添加元素，头插法"""
        # 先创建一个保存item值的节点
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将__head指向node
            self.__head = node
        else:
            # 将新节点的链接域next指向头节点，即_head指向的位置
            node.next = self.__head
            # 将__head的头节点的prev指向node
            self.__head.prev = node
            # 将链表的头_head指向新节点
            self.__head = node

    def append(self, item):
        """尾部添加元素，尾插法"""
        # 先创建一个保存item值的节点
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
        else:
            # 若不为空，则找到尾部，将尾结点的next指向新节点
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos < 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            # 先创建一个保存item值的节点
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将新节点node的next指向插入位置的节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next is None:
                    # 如果链表只有这一个节点
                    self.__head = Node
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将__head指向第二个节点
                    self.__head = cur.next
                return
            while cur is not None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


# 测试双向链表
if __name__ == "__main__":
    # 创建单向链表
    Dll = DoubleLinkList()
    # 添加元素
    Dll.add(1)
    Dll.add(2)
    Dll.append(3)
    Dll.insert(2, 4)
    print('length:', Dll.length())
    # 遍历
    Dll.travel()
    # 查找元素
    print(Dll.search(3))
    print(Dll.search(5))
    # 删除元素
    Dll.remove(1)
    print("length:", Dll.length())
    Dll.travel()
