# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 21:23
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pFast = head
        pSlow = head
        while pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast == pSlow:
                break
        if pFast == None or pFast.next == None:
            return None
        pFast = head
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast


# 测试:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.detectCycle(node1).val)
