# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):   # 借O(n)的辅助空间.
        # write code here
        if not pRootOfTree:
            return
        self.attr = []
        self.Inorder(pRootOfTree)
        for k, v in enumerate(self.attr[:-1]):
            self.attr[k].right = self.attr[k+1]
            self.attr[k+1].left = v
        return self.attr[0]

    def Inorder(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Inorder(pRootOfTree.left)
        self.attr.append(pRootOfTree)
        self.Inorder(pRootOfTree.right)

"""
解题思路一：由于输入的一个二叉搜索树，其左子树大于右子树的值，这位后面的排序做了准备，因为只需要中序遍历即可，将所有的节点保存到一个列表，。对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。
借助了一个O（n）的辅助空间 
（注意：attr列表中的元素是链表节点）
"""

class Solution1:
    def Convert(self, pRootOfTree):  # 递归 , 按照左右子树分治，递归实现
        # write code here
        if not pRootOfTree:
            return
        pHead = root = pRootOfTree
        while pHead.left:
            pHead = pHead.left
        self.Core(root)
        return pHead

    def Core(self, root):
        if not root.left and not root.right:
            return
        if root.left:
            Preroot = root.left
            self.Core(root.left)
            while Preroot.right:
                Preroot = Preroot.right
            Preroot.right = root
            root.left = Preroot
        if root.right:
            nextRoot = root.right
            self.Core(root.right)
            while nextRoot.left:
                nextRoot = nextRoot.left
            nextRoot.left = root
            root.right = nextRoot

"""
解题思路二：递归，将特定节点的左指针指向其左子树中的最后子节点，将其右指针指向其右子树中的最左子节点，依次递归，调整好全部节点的指针指向。
"""

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
newList = S.Convert(pNode1)
print(newList.val)