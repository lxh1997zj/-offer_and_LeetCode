# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.'

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s or len(s) <= 0:
            return -1
        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        for key, value in enumerate(s):
            if char_dict[value] == 1:
                return key
        return -1