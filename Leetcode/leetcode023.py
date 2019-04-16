# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/16 16:20
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists): # List[ListNode]) -> ListNode:  # 分治法
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]
        else:
            head1 = self.mergeKLists(lists[: len(lists)//2])
            head2 = self.mergeKLists(lists[len(lists)//2:])
            return self.mergeTwoLists(head1, head2)

    def mergeTwoLists(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val < head2.val:
            res = head1
            res.next = self.mergeTwoLists(head1.next, head2)
        else:
            res = head2
            res.next = self.mergeTwoLists(head1, head2.next)
        return res


class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  # 构建最小堆
        import heapq
        heap = []
        for l in lists:
            if l != None:
                heap.append((l.val,l))
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _,h = heapq.heappop(heap)
            cur.next = h
            cur = cur.next
            if h.next:
                heapq.heappush(heap,(h.next.val,h.next))
        return dummy.next
