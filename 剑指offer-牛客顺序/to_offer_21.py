# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）'

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            # 相当于元素进栈后立即出栈
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            # 如果当前辅助栈中的栈顶元素刚好是要弹出的元素，那么直接弹出
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 不断往辅助栈中压入元素
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True

"""
可以手写模拟以下！
参考：https://github.com/leeguandong/Interview-code-practice-python/blob/master/%E5%89%91%E6%8C%87offer/%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py
"""


class Solution1:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            if stack[-1] != popV[0]:
                continue
            else:
                stack.pop()
                popV.pop(0)
        while len(stack) > 0 and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        if len(stack) == 0:
            return True
        else:
            return False


class Solution2:
    def IsPopOrder(self, pushV, popV):  # 此方法为Solution1的优化.
        # write code here
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True
