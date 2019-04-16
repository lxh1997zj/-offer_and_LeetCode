# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/13 18:01
'''

"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in m:
                i = max(m[s[j]], i)
            ans = max(ans, j-i+1)
            m[s[j]] = j + 1
        # print(m)
        return ans


# 测试:
s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
