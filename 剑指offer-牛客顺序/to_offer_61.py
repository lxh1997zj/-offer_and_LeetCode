# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/6 17:29
'''

"""请实现两个函数，分别用来序列化和反序列化二叉树"""

"""
解题思路：
首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，再碰到左子节点或者右子节点为None的时候输出一个特殊字符”#”。对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。当遇到当前指向的字符为特殊字符”#”或者指针超出了序列的长度，则返回None，指针后移，继续遍历。
"""


# 得先读懂题目的意思！
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        lis = s.split(',')
        if self.flag >= len(s):
            return None
        root = None
        if lis[self.flag] != '#':
            root = TreeNode(int(lis[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


class Solution1:
    def Serialize(self, root):  # 这个采用非递归去序列化二叉树
        # write code here
        SerializeStr = ''
        if not root:
            return '#'
        stack = []
        while root or stack:
            while root:
                SerializeStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            SerializeStr += '#,'
            root = stack.pop()
            root = root.right
        # print(SerializeStr)
        SerializeStr = SerializeStr[:-1]
        return SerializeStr

    def Deserialize(self, s):
        # write code here
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp+1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp


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

s = Solution()
print(s.Serialize(pNode1))  # 8,6,5,#,#,7,#,#,10,9,#,#,11,#,#
print('-----------------')
a = s.Serialize(pNode1)
print(s.Deserialize(a).val)  # 8

print('==========================')

s1 = Solution1()
print(s1.Serialize(pNode1))
print('------------------')
b = s1.Serialize(pNode1)
print(s1.Deserialize(b).val)
