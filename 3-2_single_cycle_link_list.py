# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 3-2_single_cycle_link_list.py
@time: 2020/10/28 9:30
@description:
"""


class Node(object):
    """单向循环链表的结点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表实现（单向循环链表的操作）：
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
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数据
        count = 1
        while cur.next != self.__head:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=',')
            cur = cur.next
        # 退出循环，cur指向尾结点，但尾结点的元素未打印
        print(cur.item)
        print()

    def add(self, item):
        """头部添加元素，头插法"""
        # 先创建一个保存item值的节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = self.__head

    def append(self, item):
        """尾部添加元素，尾插法"""
        # 先创建一个保存item值的节点
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
            node.next = node
        # 若不为空，则找到尾部，将尾结点的next指向新节点
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

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
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            # 如果找到了指定元素
            if cur.item == item:
                if cur == self.__head:
                    # 头节点的情况
                    # 需要找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点，接下来处理尾节点
        if cur.item == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                # 链表不止一个节点
                pre.next = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        if cur.item == item:
            return True
        return False


# 测试单向链表
if __name__ == "__main__":
    # 创建单向链表
    ll = SingleCycleLinkList()
    # 添加元素
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print('length:', ll.length())
    # 遍历
    ll.travel()
    # 查找元素
    print(ll.search(2))
    print(ll.search(6))
    print(ll.search(100))
    # 删除元素
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
