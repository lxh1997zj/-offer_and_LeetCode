# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个链表，输出该链表中倒数第k个结点。'

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        pAhead = head
        pBhead = None
        for i in range(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None
        pBhead = head
        while pAhead.next:
            pAhead = pAhead.next
            pBhead = pBhead.next
        return pBhead

"""
解题思路：为了实现只遍历链表一次就能找到倒数第k个节点，我们可以定义两个指针。让第一个指针先向前走k-1步，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1,当第一个指针到达链表的尾节点时，第二个指针刚好到达倒数第k个节点。
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
"""