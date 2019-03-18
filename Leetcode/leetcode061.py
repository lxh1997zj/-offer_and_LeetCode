# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'https://blog.csdn.net/yangjingjing9/article/details/76549063'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:        # 60ms
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head == None:
            return head
        dummy = ListNode(0)  # 创建一个虚假的头节点
        dummy.next = head    # 虚假头节点指向head
        p = dummy
        count = 0    # 计算链表长度
        while p.next:
            p = p.next   # 最终p将指向尾节点
            count += 1
        realstep = count - k % count   # 真实的右移数量
        p.next = head    # 将尾节点指向头节点，形成环形链表
        for i in range(realstep):
            p = p.next
        head = p.next   # 移动后的头节点
        p.next = None
        return head