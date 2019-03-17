# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。'

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


# 用两个队列实现一个栈
# class Solution:
#     def __init__(self):
#         self.queueA = []
#         self.queueB = []
#     def push(self, node):
#         self.queueA.insert(0, node)
#     def pop(self):
#         if not self.queueA:
#             return None
#         while len(self.queueA) != 1:
#             self.queueB.insert(0, self.queueA.pop())
#         self.queueA, self.queueB = self.queueB, self.queueA
#         return self.queueB.pop()


# 测试：
if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(7)
    s.push(3)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
