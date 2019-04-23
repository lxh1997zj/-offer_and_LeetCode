# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/23 16:53
'''

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
此程序还可以完善!
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:  # 这种方法超出时间限制
        n = len(s)
        step = n
        while step >= 1:
            i = 0
            while i <= n - step:
                if self.check_res(s[i:i + step]):
                    return s[i:i + step]
                else:
                    i += 1
            step += 1
        return ''

    def check_res(self, sub):
        return True if sub[::-1] == sub else False


class Solution1:
    def longestPalindrome(self, s: str) -> str:  # LeetCode上通过, 但本地通不过, 时间复杂度O(n2), 空间复杂度O(1)
        if not s or len(s) < 1:
            return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.s_length(s, i, i)
            len2 = self.s_length(s, i, i+1)
            len_mid = max(len1, len2)
            if len_mid > end - start:
                start = i - (len_mid-1) // 2
                end = i + len_mid // 2
        return s[start: end+1]

    def s_length(self, s, left, right):
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


# 测试:
# s = Solution()
# print(s.longestPalindrome('absba'))
# print(s.longestPalindrome('abcd'))
# print(s.longestPalindrome('abbs'))
print('----------------------------')
s1 = Solution()
print(s1.longestPalindrome('absba'))
print(s1.longestPalindrome('abbs'))
print(s1.longestPalindrome('abcd'))
