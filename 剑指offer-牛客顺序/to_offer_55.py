# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 20:56
'''
"""给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。"""

"""
解题分析：其实此题可以分解为三个题目：1）如何判断一个链表中是否包含环？2）如何找到环的入口节点？3）如何得到环中节点的数目？
解决此题：可以设置两个指针，一快一慢。
1.两个指针一个fast、一个slow同时从一个链表的头部出发
  fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇，（如果相遇就证明此链表包含环，否则没有环，解决问题1）
2.1 此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
    这次两个指针一次走一步，相遇的地方就是入口节点（解决问题2，得到环的入口节点）。
2. 2 接着步骤1，如果两个指针相遇，必然在环内，所以可以从这个节点出发，一遍继续向前移动，一遍计数，当再次回到这个节点时，就可以得到环中节点数了（解决问题3，得到环中节点数目）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        pFast = pHead
        pSlow = pHead
        while pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast == pSlow:
                break
        if pFast == None or pFast.next == None:
            return None
        pFast = pHead
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
print(s.EntryNodeOfLoop(node1).val)
print('--------------------------')


"""
拓展：
在前一题的基础上，如何得到环中节点的数目？
"""


class Solution1:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        pFast = pHead
        pSlow = pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast == None or pFast.next == None:
            return None
        meetindNode = pFast
        nodesInLoop = 1
        while pFast.next != meetindNode:
            pFast = pFast.next
            nodesInLoop += 1
        return nodesInLoop


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

s = Solution1()
print(s.EntryNodeOfLoop(node1))
