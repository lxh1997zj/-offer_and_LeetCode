# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/7 15:31
'''

"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
"""

"""解题思路：中序遍历"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):    # 非递归实现中序遍历
        # write code here
        if not pRoot or k <= 0:
            return None
        pNode = pRoot
        res, stack = [], []
        while pNode or len(stack):
            while pNode:
                stack.append(pNode)
                pNode = pNode.left
            if len(stack):
                pNode = stack.pop()
                res.append(pNode)
                pNode = pNode.right
        if k > len(res):
            return None
        return res[k-1]


class Solution1:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):   # 递归实现中序遍历
        # write code here
        if not pRoot or k <= 0:
            return None
        res = []
        def inOrder(pRoot):
            if not pRoot:
                return None
            inOrder(pRoot.left)
            res.append(pRoot)
            inOrder(pRoot.right)
        inOrder(pRoot)
        if k > len(res):
            return None
        return res[k-1]


# 测试:
pNode1 = TreeNode(5)
pNode2 = TreeNode(3)
pNode3 = TreeNode(7)
pNode4 = TreeNode(2)
pNode5 = TreeNode(4)
pNode6 = TreeNode(6)
pNode7 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
print(s.KthNode(pNode1, 3).val)
print('----------------------')
s1 = Solution1()
print(s1.KthNode(pNode1, 3).val)
