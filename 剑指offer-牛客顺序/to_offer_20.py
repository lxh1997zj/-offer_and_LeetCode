# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1）），在该栈中，调用min、push、pop的时间复杂度都是O(1)'

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())
    def pop(self):
        # write code here
        if self.stack == [] or self.minstack == []:
            return
        self.stack.pop()
        self.minstack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]
"""
把每次的最小元素保存起来放在另一个辅助栈里.
引入两个栈，一个栈每次push实际的数字，另一个minStack，如果push的数字小于minStack栈顶的数字，push新的数字，否则就繁殖，把最小栈栈顶的数字再压入一遍。
"""
S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())