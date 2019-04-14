# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/14 16:25
'''
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

注意: 反转后的数也应在[-2^31, 2^31-1]中。
"""


class Solution(object):
    def reverse(self, x):  # 36ms
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        temp = 0
        new_x = abs(x)
        while new_x != 0:
            temp = temp * 10 + new_x % 10
            new_x //= 10
        temp = temp if x >= 0 else -temp
        if temp >= -2 ** 31 and temp <= 2 ** 31 - 1:
            return temp
        else:
            return 0

    def hhh(self, x):   # 40ms
        a = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return a if -2 ** 31 <= a <= 2 ** 31 - 1 else 0


# 测试:
s = Solution()
print(s.reverse(123))
print(s.hhh(123))
print(s.reverse(-123))
print(s.hhh(-123))
print(s.reverse(1534236469))
print(s.hhh(1534236469))
