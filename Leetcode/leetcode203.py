# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# class ListNode:
#	def __init__(self,x):
#		self.val = x
#		self.next = None

class Solution:
	"""
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
	def removeElements(self,head,val):
		"""
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
		pre_node = ListNode(None)
		pre_node.next = head
		q = pre_node
		while q.next:
			if q.next.val == val:
				q.next = q.next.next
			else:
				q = q.next
		return pre_node.next