# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）'

"""解题思路：递归，注意空指针的情况。"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        # 当Tree1和Tree2都不为零的时候，才进行比较。否则直接返回false
        if pRoot1 and pRoot2:
            # 如果找到了对应Tree2的根节点的点
            if pRoot1.val == pRoot2.val:
                # 以这个根节点为为起点判断是否包含Tree2
                res = self.isequalSubtree(pRoot1, pRoot2)
            # 如果找不到，那么就再去root的左儿子当作起点，去判断时候包含Tree2
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            # 如果还找不到，那么就再去root的右儿子当作起点，去判断时候包含Tree2
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res
    """
    用于递归判断树的每个节点是否相同
    需要注意的地方是: 前两个if语句不可以颠倒顺序
    如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    """
    def isequalSubtree(self, pRoot1, pRoot2):
        # 如果Tree2已经遍历完了都能对应的上，返回true
        if pRoot2 == None:
            return True
        # 如果Tree2还没有遍历完，Tree1却遍历完了。返回false
        if pRoot1 == None:
            return False
        # 如果其中有一个点没有对应上，返回false
        if pRoot1.val != pRoot2.val:
            return False
        # 如果根节点对应的上，那么就分别去子节点里面匹配
        return self.isequalSubtree(pRoot1.left, pRoot2.left) and self.isequalSubtree(pRoot1.right, pRoot2.right)
"""
思路：参考剑指offer
1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
剩下的代码不会执行，如果匹配不成功，默认返回false
2、递归思想，如果根节点相同则递归调用DoesTree1HaveTree2（），
如果根节点不相同，则判断tree1的左子树和tree2是否相同，
再判断右子树和tree2是否相同
3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
tree1为空有两种情况（1）如果tree1为空&&tree2不为空说明不匹配，
（2）如果tree1为空，tree2为空，说明匹配。
"""
