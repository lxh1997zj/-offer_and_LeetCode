# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/20 23:05
'''

"""判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。"""


class Solution:
    def isPalindrome(self, x):  # : int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x //= 10
        return x == res or x == res // 10

# 测试:
s = Solution()
print(s.isPalindrome(12321))
print(s.isPalindrome(-12321))
print(s.isPalindrome(123456))
