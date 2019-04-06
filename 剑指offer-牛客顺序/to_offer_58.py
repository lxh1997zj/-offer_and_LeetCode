# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/6 14:45
'''

"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

"""
解题思路：
可以定义一种遍历算法，先遍历右子节点再遍历左子节点。注意，我们必须把遍历二叉树时遇到的空指针考虑进来。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):    # 递归解法
        # write code here
        return self.isSymmetricalCore(pRoot, pRoot)

    def isSymmetricalCore(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCore(pRoot1.left, pRoot2.right) and self.isSymmetricalCore(pRoot1.right, pRoot2.left)


"""
分为递归和非递归的两种方式，思想是一样的。主要就是把叶子节点的None节点也加入到遍历当中。按照前序遍历二叉树，存入一个序列中。然后按照和前序遍历对应的先父节点，然后右子节点，最后左子节点遍历二叉树，存入一个序列。如果前后两个序列相等，那么说明二叉树是对称的。
"""


class Solution1:
    def isSymmetrical(self, pRoot):    # 非递归解法
        # write code here
        preList = self.PreOrder(pRoot)
        mirrorList = self.MirrorPreOrder(pRoot)
        if preList == mirrorList:
            return True
        return False

    def PreOrder(self, pRoot):
        if pRoot == None:
            return [None]
        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.left
                if not pNode:
                    output.append(None)
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.right
                if not pNode:
                    output.append(None)
        return output

    def MirrorPreOrder(self, pRoot):
        if pRoot == None:
            return [None]
        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.right
                if not pNode:
                    output.append(None)
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.left
                if not pNode:
                    output.append(None)
        return output


# 测试:
pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.isSymmetrical(pNode1))
print('---------------------')
"""
         8
        / \
       6   10
      / \  / \
     5   7 9  11
"""
S1 = Solution1()
print(S1.isSymmetrical(pNode1))
