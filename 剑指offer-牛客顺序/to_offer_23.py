# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。'

"""二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点"""

class Solution:
    def VerifySquenceOfBST(self, sequence):  # 递归
        # write code here
        if not sequence or len(sequence) <= 0:
            return False
        i = 0
        # 根据后续遍历的性质，尾元素必定是树的根，同时小于尾元素的值是左子树，大于尾元素的值为右子树,此时i属于右子树
        root = sequence[-1]
        for node in sequence[: -1]:
            if node > root:
                break
            i += 1
        # 如果在右子树中有比根节点小的值，直接返回False
        for node in sequence[i: -1]:
            if node < root:
                return False
        # 判断左子树是否为二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[: i])
        # 判断右子树是否为二叉搜索树
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i: -1])
        return left and right

"""
减少递归深度的办法：某段的元素个数如果<=3，则返回True；某整段的最小元素不小于尾元素或者整段的最大元素不大于尾元素，说明仅有左子树或者右子树，返回True。
"""
