# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/21 23:02
'''

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

时间复杂度: O(n)
空间复杂度: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        ex = strs[0]
        i = 1
        while i < len(strs):
            if strs[i].find(ex) != 0:
                ex = ex[: -1]
                i -= 1
            elif strs[i].find(ex) == 0:
                i += 1
            if ex == "":
                return ex
        return ex


# 测试:
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print('----')
