# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)'

"""思路：剑指offer P182"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        def FindPathCore(root, path, curNumer):
            curNumer += root.val
            path.append(root)
            flag = root.left == None and root.right == None # 判断是否为叶节点
            # 如果到达叶子节点且当前值等于期望值
            if flag and curNumer == expectNumber:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)
            if curNumer < expectNumber:
                if root.left:
                    FindPathCore(root.left, path, curNumer)
                if root.right:
                    FindPathCore(root.right, path, curNumer)
            path.pop()
        FindPathCore(root, [], 0)
        return result


class Solution1:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root.left == None and root.right == None:
            if root.val == expectNumber:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.FindPath(root.left, expectNumber-root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.FindPath(root.right, expectNumber-root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

# 此为方法二的优化版:
class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root.left == None and root.right == None:
            if root.val == expectNumber:
                return [[root.val]]
            else:
                return []
        a = self.FindPath(root.left, expectNumber-root.val) + self.FindPath(root.right, expectNumber-root.val)
        return [[root.val] + i for i in a]


# 测试:
pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

S = Solution()
print(S.FindPath(pNode1, 22))
