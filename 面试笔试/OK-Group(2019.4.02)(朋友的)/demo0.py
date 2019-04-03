# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 14:20
'''
"""leetcode-023: 合并 k 个排序链表"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  # 还有错！
        import heapq
        heap = []
        for i in lists:
            if i != None:
                heap.append((i.val, i))
        heapq.heapify(heap)
        head = ListNode(0)
        cur = head
        while heap:
            k, v = heapq.heappop(heap)
            cur.next = v
            cur = cur.next
            if v.next:
                heapq.heappush(heap, (v.next.val, v.next))
        return head.next

