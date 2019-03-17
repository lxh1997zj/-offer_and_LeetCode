# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。'

"""
解题思路：主题考虑底数为0.0，指数为负数的情况，此时可以利用全局变量指出g_InvalidInput为True,同时返回0.0
"""

class Solution:
    g_InvalidInput = False

    def Power(self, base, exponent):
        # write code here
        if base == 0.0 and exponent < 0:
            g_InvalidInput = True
            return 0.0
        if exponent >= 0:
            return self.PowerWithUnsignedExponent(base, exponent)
        return 1.0 / self.PowerWithUnsignedExponent(base, -exponent)

    def PowerWithUnsignedExponent(self, base, exponent):
        res = 1.0
        for i in range(exponent):
            res = res * base
        return res
"""
解题优化：上述代码PowerWithUnsignedExponent部分还可以优化如下：使用平方的一半*平方的一半来计算平方，此时时间复杂度为O(logn)。同时涉及除以2用右移运算符代替，判断奇偶数时用位与运算代替求余运算符，这样效率高很多。
    def PowerWithUnsignedExponent2(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.PowerWithUnsignedExponent2(base, exponent >> 1)
        res *= res
        if exponent & 0x1 == 1:
            res *= base
        return res
"""


    # def Power(self, base, exponent):
    #     # write code here
    #     result = 1.0
    #     if exponent >= 0:
    #         for i in range(exponent):
    #             result *= base
    #     else:
    #         for i in range(abs(exponent)):
    #             result *= base
    #         result = 1.0/result
    #     return result

