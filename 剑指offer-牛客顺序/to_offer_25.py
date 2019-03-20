# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）'

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):   # 递归
        # write code here
        if pHead == None:
            return None
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode

"""
注意链表结点进行复制的时候，不能简单地写作 pCloned = pNode，这样的话之后对pCloned的操作也会作用在pNode上面，导致操作循环往复。需要重新定一个pCloned = ListNode(0)，然后对结点的.val .next .random 进行设置。同时，在将复制的结点的random指向原始链表结点的random的next的时候，需要先判断一下，原始链表结点的next是否为None，不为None再指向。
"""

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution1:
    # 返回 RandomListNode
    def Clone(self, pHead):   # 分解法，方法同剑指offer--P187
        # write code here
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next
    # 将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
    # 拆分链表：将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pCloned = pNode.next
        pNode.next = pCloned.next
        pNode = pNode.next
        while pNode:
            pCloned.next = pNode.next
            pCloned = pCloned.next
            pNode.next = pCloned.next
            pNode = pNode.next
        return pClonedHead

# 测试:
node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)


# Python自带库!   真厉害！！！
class Solution2:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        import copy
        return copy.deepcopy(pHead)
"""
python中copy和deepcopy的区别:
https://blog.csdn.net/qq_32907349/article/details/52190796
"""
