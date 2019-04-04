# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/4 10:44
'''
"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pass



















print('=======================================================================')
# 拓展:
"""
题目：
删除链表中的节点
题一：
在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
解题思路：
我们要删除节点i,先把i的下一个节点j的内容复制到i,然后把i的指针指向节点j的下一个节点。此时再删除节点j,其效果等同于把节点i删除了。
"""

"""此程序还存在问题，删除的结点被删除后不为None！"""


class ListNode1:
    def __init__(self, x):
        self.value = x
        self.next_node = None
class Solution2:
    def delete_node(self,head_node,del_node):
        """
        删除指定节点
        """
        if not (head_node and del_node):
            return None
        # 要删除的节点不是尾节点
        if del_node.next_node:
            del_next_node = del_node.next_node
            del_node.value = del_next_node.value
            del_node.next_node = del_next_node.next_node
            del_next_node.value = None
            del_next_node.next_node = None
        # 链表只要一个节点，删除头节点（也是尾节点）
        elif del_node == head_node:
            head_node.next_node = None
            head_node.value = None
            del_node.next_node = None
            del_node.value = None
        # 链表中有多个节点，删除尾节点
        else:
            node = head_node
            while node.next_node != del_node:
                node = node.next_node
            node.next_node = None
            del_node.next_node = None
            del_node.value = None

        return head_node

# 测试:
node1 = ListNode1(10)
node2 = ListNode1(11)
node3 = ListNode1(13)
node4 = ListNode1(15)
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

S = Solution2()
# S.delete_node(node1, node3)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node2)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node1)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node1)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print(node1 == None)
# print('------------------')
S.delete_node(node1, node4)
print(node1.value)
print(node2.value)
print(node3.value)
print(node4.value)
print(node4 == None)
print('------------------')
