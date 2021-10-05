# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 7-1_binary_tree.py
@time: 2020/11/20 18:57
@description:
"""


class Node(object):
    """树的节点"""
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class BinaryTree(object):
    """二叉树的实现"""
    def __init__(self):
        self.root = None

    def add(self, item):
        """往数中添加节点"""
        # 创建节点
        node = Node(item)
        # 判断是否有根节点
        if self.root is None:
            self.root = node
            return
        # 创建遍历队列
        queue = [self.root]
        # 遍历（广度优先）
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left_child is None:  # 遍历当前节点的左孩子
                cur_node.left_child = node
                return
            else:
                queue.append(cur_node.left_child)

            if cur_node.right_child is None:  # 遍历当前节点的右孩子
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def breadth_travel(self):
        """广度优先遍历（层次遍历）"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self, node):
        """深度优先遍历（前序遍历）"""
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def inorder(self, node):
        """深度优先遍历（中序遍历）"""
        if node is None:
            return
        self.inorder(node.left_child)
        print(node.item, end=" ")
        self.inorder(node.right_child)

    def postorder(self, node):
        """深度优先遍历（中序遍历）"""
        if node is None:
            return
        self.postorder(node.left_child)
        self.postorder(node.right_child)
        print(node.item, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
