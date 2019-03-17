# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'操作给定的二叉树，将其变换为源二叉树的镜像。'

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):  # 递归实现
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        if root.left:            # 可以不进行if判断直接循环
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)

class Solution1:
    # 返回镜像树的根节点
    def Mirror(self, root):  # 非递归，用栈实现！
        # write code here
        if not root:
            return
        stackNode = []
        stackNode.append(root)
        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum += 1

class Solution2:
    # 返回镜像树的根节点
    def Mirror(self, root):  # 非递归，用队列实现！
        # write code here
        if not root:
            return
        queueNode = [root]
        while len(queueNode) > 0:
            cur, count = len(queueNode), 0
            while count < cur:
                count += 1
                pRoot = queueNode.pop(0)
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.left:
                    queueNode.append(pRoot.left)
                if pRoot.right:
                    queueNode.append(pRoot.right)