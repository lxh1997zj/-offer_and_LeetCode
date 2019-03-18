# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。输入3输出3，输入11输出0.'

'''
参考url = 'https://blog.csdn.net/liuxiao214/article/details/77949837?utm_source=blogxgwz10'
class Solution(object):  # 52ms
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit=1
        base=9
        ith=1
        while n>base*digit:
            n=n-base*digit
            digit=digit+1
            ith=ith+base
            base=base*10
        return ord(str(ith+(n-1)/digit)[(n-1)%digit])-ord('0')
'''
# 我自己想的
class Solution:   # 48ms
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c = 1,9,1
        while n > a*b:
            n = n - a*b
            a = a + 1
            c = c + b
            b = b * 10
        t = c + (n-1)//a
        x = (n-1) % a
        return int(str(t)[x])
s = Solution()
print(s.findNthDigit(100))