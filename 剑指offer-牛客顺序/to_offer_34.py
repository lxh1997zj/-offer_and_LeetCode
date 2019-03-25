# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.'

"""先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。"""

class Solution:
    def FirstNotRepeatingChar(self, s):  # 自定义一个哈希表，键值key为字符，值value为该字符出现的次数
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


class Solution1:
    def FirstNotRepeatingChar(self, s):   # 利用python特性.
        # write code here
        if not s or len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1

# 测试:
s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))
print('----------------------------------')
s = Solution1()
print(s.FirstNotRepeatingChar('abaccdeff'))
print('----------------------------------')


"""
题目拓展：字符流中第一个只出现一次的字符。
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符流没有存在出现一次的字符，返回#字符。
"""

class Solution2:
    # 引入两个辅助空间：alist数组存储当前读入字符流的字符（按顺序）
    # char_dict存储字符出现的次数，如果字符出现大于1次，为简单起见，统一记为2次。
    def __init__(self):
        self.alist = []
        self.char_dict = {}

    def FirstNotRepeatingChar(self):
        while len(self.alist) > 0 and self.char_dict[self.alist[0]] > 1:
            self.alist.pop(0)
        if len(self.alist) > 0:
            return self.alist[0]
        return '#'

    def Insert(self, char):
        if char not in self.char_dict.keys():
            self.char_dict[char] = 1
            self.alist.append(char)
        else:
            self.char_dict[char] =2

# 测试:
s = Solution2()
for i in 'google':
    s.Insert(i)
print(s.FirstNotRepeatingChar())
