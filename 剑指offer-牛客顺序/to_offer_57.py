# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/4 17:08
'''

"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

"""
解题思路: 剑指offer-P65页
三种情况：
当前节点有右子树的话，当前节点的下一个结点是右子树中的最左子节点；当前节点无右子树但是是父节点的左子节点，下一个节点是当前结点的父节点；当前节点无右子树而且是父节点的右子节点，则一直向上遍历，直到找到最靠近的一个祖先节点pNode，pNode是其父节点的左子节点，那么输入节点的下一个结点就是pNode的父节点。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return
        # 如果该节点有右子树，那么下一个节点就是它右子树中的最左节点
        elif pNode.right != None:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 如果一个节点没有右子树，，并且它还是它父节点的右子节点
        elif pNode.next != None and pNode.next.right == pNode:
            while pNode.next != None and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next
        # 如果一个节点是它父节点的左子节点，那么直接返回它的父节点
        else:
            return pNode.next


# 测试:
tree1 = TreeLinkNode(1)
tree2 = TreeLinkNode(2)
tree3 = TreeLinkNode(3)
tree4 = TreeLinkNode(4)
tree5 = TreeLinkNode(5)
tree6 = TreeLinkNode(6)
tree7 = TreeLinkNode(7)
tree8 = TreeLinkNode(8)
tree9 = TreeLinkNode(9)

tree1.left = tree2
tree1.right = tree3
tree1.next = None

tree2.left = tree4
tree2.right = tree5
tree2.next = tree1

tree3.left = tree6
tree3.right = tree7
tree3.next = tree1

tree4.left = None
tree4.right = None
tree4.next = tree2

tree5.left = tree8
tree5.right = tree9
tree5.next = tree2

tree6.left = None
tree6.right = None
tree6.next = tree3

tree7.left = None
tree7.right = None
tree7.next = tree3

tree8.left = None
tree8.right = None
tree8.next = tree5

tree9.left = None
tree9.right = None
tree9.next = tree5

s = Solution()
print(s.GetNext(tree9).val)
print(s.GetNext(tree2).val)
print(s.GetNext(tree1).val)
print(s.GetNext(tree4).val)
