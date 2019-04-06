# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/6 16:41
'''

"""从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。"""

"""思路参考: to_offer_22.py 拓展1"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        nodes = [pRoot]
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            res.append(curStack)
            nodes = nextStack
        return res


class Solution1:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):    # 同剑指offer解法
        # write code here
        if not pRoot:
            return []
        res, res_val = [], []
        res.append(pRoot)
        nextLever = 0
        toBePrint = 1
        temp = []
        while len(res) > 0:
            node = res.pop(0)
            temp.append(node.val)
            if node.left:
                res.append(node.left)
                nextLever += 1
            if node.right:
                res.append(node.right)
                nextLever += 1
            toBePrint -= 1
            if toBePrint == 0:
                res_val.append(temp)
                toBePrint = nextLever
                nextLever = 0
                temp = []
        return res_val


class Solution2:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):      # 思路同Solution
        # write code here
        if not pRoot:
            return []
        res, nodes = [], [pRoot]
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
print(S.Print(pNode1))
print('-------------')
S1 = Solution1()
print(S1.Print(pNode1))
print('-------------')
S2 = Solution2()
print(S2.Print(pNode1))
