# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。'

"""
解题思路：
1.如果一棵树只有一个节点，它的深度为1
2.如果根节点只有左子树而没有右子树，那么树的深度是左子树的深度加1
同样，如果根节点只有右子树而没有左子树，那么树的深度是右子树的深度加1
既有右子树又有左子树时，数的深度是左子树和右子树深度较大者加1
利用递归很容易实现上述思路：
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):  # 递归解法, 简单直接, 时间复杂度O(n), 空间复杂度O(log n)
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1


# 非递归算法，利用一个栈以及一个标志位栈
class Solution1:
    def TreeDepth(self, pRoot):  # 非递归，利用两个栈.
        if not pRoot:
            return 0
        stack, tag = [], []
        depth, pNode = 0, pRoot
        while pNode or stack:
            while pNode:
                stack.append(pNode)
                tag.append(0)
                pNode = pNode.left
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                pNode = None
            else:
                pNode = stack[-1]
                pNode = pNode.right
                tag.pop()
                tag.append(1)
        return depth

# 测试:
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution()
print(S.TreeDepth(pNode1))
print('-----------------')
S = Solution1()
print(S.TreeDepth(pNode1))