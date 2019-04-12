# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/12 14:44
'''

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        temp = ans
        tempSum = 0
        while True:
            if l1:
                tempSum += l1.val
                l1 = l1.next
            if l2:
                tempSum += l2.val
                l2 = l2.next
            temp.val = tempSum % 10
            tempSum //= 10
            if not l1 and not l2 and tempSum == 0:
                break
            temp.next = ListNode(0)
            temp = temp.next
        return ans


# 测试:
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(6)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

S = Solution()
print(S.addTwoNumbers(node1, node4).val)
print(S.addTwoNumbers(node1, node4).next.val)
print(S.addTwoNumbers(node1, node4).next.next.val)
print(S.addTwoNumbers(node1, node4).next.next.next.val)
