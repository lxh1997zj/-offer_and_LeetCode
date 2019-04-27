# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/27 23:22
'''

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            res = l2
            res.next = self.mergeTwoLists(l1, l2.next)
        else:
            res = l1
            res.next = self.mergeTwoLists(l1.next, l2)
        return res


# 测试:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6

s = Solution()
print(s.mergeTwoLists(node1, node4).val)
print(s.mergeTwoLists(node1, node4).next.val)
