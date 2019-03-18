# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):  # 相当于按层遍历, 中间需要队列做转存
        # write code here
        if not root:
            return []
        res, res_val = [], []   # res为队列
        res.append(root)
        while len(res) > 0:
            node = res.pop(0)
            res_val.append(node.val)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res_val

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
print(S.PrintFromTopToBottom(pNode1))


print('-----------------------------------------------------------------------')
"""
题目拓展一：分行从上到下打印二叉树。
题：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# method1:
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, res_val = [], []
        res.append(pRoot)
        nextLevel = 0  # 表示下一层的结点数
        tobePrint = 1  # 表示还没被写入的结点数
        temp = []
        while len(res) > 0:
            node = res.pop(0)
            temp.append(node.val)
            if node.left:
                res.append(node.left)
                nextLevel += 1
            if node.right:
                res.append(node.right)
                nextLevel += 1
            tobePrint -= 1
            if tobePrint == 0:
                res_val.append(temp)
                tobePrint = nextLevel
                nextLevel = 0
                temp = []
        return res_val

# method2:
class Solution1:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, nodes= [], [pRoot]
        while nodes:
            curstack, nextstack = [], []
            for node in nodes:
                curstack.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            res.append(curstack)
            nodes = nextstack
        return res

# method3(思路同方法2):
class Solution2:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, nodes= [], [pRoot]
        count = 0
        while count < len(nodes):
            temp = []
            last = len(nodes)
            while count < last:
                temp.append(nodes[count].val)
                if nodes[count].left:
                    nodes.append(nodes[count].left)
                if nodes[count].right:
                    nodes.append(nodes[count].right)
                count += 1
            res.append(temp)
        return res

# 测试:
# pNode1 = TreeNode(8)
# pNode2 = TreeNode(6)
# pNode3 = TreeNode(10)
# pNode4 = TreeNode(5)
# pNode5 = TreeNode(7)
# pNode6 = TreeNode(9)
# pNode7 = TreeNode(11)
# pNode1.left = pNode2
# pNode1.right = pNode3
# pNode2.left = pNode4
# pNode2.right = pNode5
# pNode3.left = pNode6
# pNode3.right = pNode7
# S = Solution()
# print(S.Print(pNode1)


print('-----------------------------------------------------------------------')
"""
题目拓展二：之字形打印二叉树
题：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:                   # method1
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, nodes= [], [pRoot]
        left_to_right = True
        while nodes:
            curstack, nextstack = [], []
            for node in nodes:
                curstack.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            if not left_to_right:
                curstack.reverse()
            res.append(curstack)
            left_to_right = not left_to_right
            nodes = nextstack
        return res

# method2(同剑指offer):
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, nodes= [], [pRoot]
        right = True
        while nodes:
            curstack, nextstack = [], []
            if right:
                for node in nodes:
                    curstack.append(node.val)
                    if node.left:
                        nextstack.append(node.left)
                    if node.right:
                        nextstack.append(node.right)
            else:
                for node in nodes:
                    curstack.append(node.val)
                    if node.right:
                        nextstack.append(node.right)
                    if node.left:
                        nextstack.append(node.left)
            res.append(curstack)
            nextstack.reverse()
            right = not right
            nodes = nextstack
        return res

# 测试:
# pNode1 = TreeNode(8)
# pNode2 = TreeNode(6)
# pNode3 = TreeNode(10)
# pNode4 = TreeNode(5)
# pNode5 = TreeNode(7)
# pNode6 = TreeNode(9)
# pNode7 = TreeNode(11)
# pNode1.left = pNode2
# pNode1.right = pNode3
# pNode2.left = pNode4
# pNode2.right = pNode5
# pNode3.left = pNode6
# pNode3.right = pNode7
# S = Solution()
# print(S.Print(pNode1))