# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 20:34
'''
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符流没有存在出现一次的字符，返回#字符。
"""

"""
以前做过, to_offer_34.py
"""


class Solution:
    # 返回对应char
    def __init__(self):
        # 引入两个辅助空间：a_list数组存储当前读入字符流的字符（按顺序）
        # char_dict存储字符出现的次数，如果字符出现大于1次，为简单起见，统一记为2次。
        self.a_list = []
        self.char_dict = {}
    def FirstAppearingOnce(self):
        # write code here
        while len(self.a_list) > 0 and self.char_dict[self.a_list[0]] > 1:
            self.a_list.pop(0)
        if len(self.a_list) > 0:
            return self.a_list[0]
        return '#'

    def Insert(self, char):
        # write code here
        if char not in self.char_dict.keys():
            self.char_dict[char] = 1
            self.a_list.append(char)
        else:
            self.char_dict[char] = 2


# 测试:
s = Solution()
for i in 'google':
    s.Insert(i)
print(s.FirstAppearingOnce())
print('--------------------')
s1 = Solution()
for j in 'go':
    s1.Insert(j)
print(s1.FirstAppearingOnce())
