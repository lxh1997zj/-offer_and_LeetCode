# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。'

class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = (n-1) & n
            count += 1
        return count
"""
最佳方法：把一个整数减去1，再和原整数做“与运算”，会把该整数最右边的1变成0。那么一个整数的二进制中表示中有多少个1，就可以进行多少次这样的操作。
注意：如果该整数是负数，要把它和0xffffffff相与，消除负数的影响。
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n & 0xffffffff).count('1')

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示.

# 测试：
s = Solution()
print(s.NumberOf1(8))
print(s.NumberOf1(12))
print(s.NumberOf1(-4))
print(s.NumberOf1(4294967292))