# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'用递归算法实现斐波那契数列: 1, 1, 2, 3, 5, 8, 13, ......,第30个数是多少?'


class Solution:
    def Fibonacci(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

# 测试:
s = Solution()
print(s.Fibonacci(30))
