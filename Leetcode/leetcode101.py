# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'参考url1 = https://blog.csdn.net/coder_orz/article/details/51579528'
'参考url2 = https://blog.csdn.net/qqxx6661/article/details/75332482'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, a, b):  # 52ms(递归)
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

'''
class Solution:
    def isSymmetric(self, root):  # 52ms(非递归算法,算是将上面的递归方法改写成非递归方法,实际上是深度优先搜索(DFS))
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            stackl.append(left.left)
            stackl.append(left.right)
            stackr.append(right.right)
            stackr.append(right.left)
        return len(stackl) == 0 and len(stackr) == 0
'''
'''
class Solution:
    def isSymmetric(self, root):   # 52ms(广度优先搜索BFS)
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queuel, queuer = [root.left], [root.right]
        while len(queuel) > 0 and len(queuer) > 0:
            left = queuel.pop()
            right = queuer.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            queuel.insert(0, left.left)
            queuel.insert(0, left.right)
            queuer.insert(0, right.right)
            queuer.insert(0, right.left)
        return len(queuel) == 0 and len(queuer) == 0
'''
'''
class Solution:
    def isSymmetric(self, root):  # 84ms(迭代) 运行速度超级慢!
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            value = [i.val if i else None for i in queue]
            if value != value[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
'''