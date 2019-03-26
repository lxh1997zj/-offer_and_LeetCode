# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入两个链表，找出它们的第一个公共结点。'

"""公共的节点，说明公共节点的值和next都是一样的，所以一定会有公共的尾部。"""

"""
①蛮力法：在第一个链表上顺序遍历每个节点，每遍历到一个节点，就在第二个链表上顺序遍历每个节点，直到找到第二个链表上有节点和第一个链表上的节点一样停止。（O(mn)）
②如果从两个链表的尾部开始往前比较（后进先出），那么最后一个相同节点就是我们要找的节点，为此可以借助两个栈，栈顶元素都一样则pop出去，直到找到最后一个相同的元素为止。（时间复杂度O(m+n),且需要额外辅助空间）
③首先遍历两个链表得到它们的长度，如果m>n，则m链表先走m-n步，然后两个链表再同时走，直到找到第一个相同的节点（即为它们的第一个公共节点）。（推荐，时间复杂度O(m+n),且不需要额外辅助空间）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):  # 时间复杂度O(m+n), 但是不需要额外空间
        # write code here
        if not pHead1 or not pHead2:
            return None
        length1 = self.HeadLength(pHead1)
        length2 = self.HeadLength(pHead2)
        if length1 > length2:
            headLong = pHead1
            headShort = pHead2
        else:
            headLong = pHead2
            headShort = pHead1
        diff = abs(length1 - length2)
        for i in range(diff):
            headLong = headLong.next
        while headLong != None and headShort != None and headLong != headShort:
            headLong = headLong.next
            headShort = headShort.next
        return headLong

    def HeadLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length


class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):  # 时间复杂度O(m+n), 但是需要额外空间
        # write code here
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        first = None                # 这里可以在设置一个数组来存放相同的结点，最后一个相同的结点就是第一个公共结点
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 == node2:
                first = node1
            else:
                break
        return first

        # 另外在开辟一个新数组存放相同的结点:
        # res = []
        # if node1 == node2:
        #     res.append(node1)
        # if res:
        #     node = res.pop()
        # return node
