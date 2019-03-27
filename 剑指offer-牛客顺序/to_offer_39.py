# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一棵二叉树，判断该二叉树是否是平衡二叉树。'

"""基于二叉树的深度，再次进行递归。以此判断左子树的高度和右子树的高度差是否大于1，若是则不平衡，反之平衡。"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return  max(left, right) + 1

    def IsBalanced_Solution(self, pRoot):   # 基于二叉树的深度，再次递归
        # write code here
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        diff = abs(left - right)
        if diff > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


class Solution1:
    def __init__(self):
        self.flag = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.TreeDepth(pRoot)
        return self.flag

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = 1 + self.TreeDepth(pRoot.left)
        right = 1 + self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return left if left > right else right


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
print(S.IsBalanced_Solution(pNode1))
print('---------------------------')
S = Solution1()
print(S.IsBalanced_Solution(pNode1))
