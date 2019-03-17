# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。'

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        """
        new_s = '' # 方法一
        for i in range(len(s)):
            if s[i] == ' ':
                new_s += '%20'
            else:
                new_s += s[i]
        return new_s
        """
        s = list(s)
        count = 0
        for i in s:
            if i == ' ':
                count += 1
        p1 = len(s) - 1    # p1是原始字符串的末尾索引
        s += [' '] * (count * 2)
        p2 = len(s) - 1    # p2是新字符串的末尾索引
        while p1 >= 0:
            if s[p1] == ' ':
                for i in ['0', '2', '%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s)
