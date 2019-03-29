# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！'


class Solution:
    def LeftRotateString(self, s, n):  # 利用python特性.
        # write code here
        if not s or len(s) < n or n < 0:
            return ''
        return s[n:] + s[:n]


"""
1.首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后根据题目中给出的左旋转字符串的个数n，用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分别旋转前[:length-n]子串和[length-n:]子串，重新拼接两个子串即可。
2.翻转两次，首先确定左旋次数n,分别翻转[:n]和[n:],合并成一个新的数组，在对新的数组进行翻转!
"""


class Solution1:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < n or n <0:
            return ''
        list_s = list(s)
        first = self.Reverse(list_s[:n])
        behind = self.Reverse(list_s[n:])
        return ''.join(self.Reverse(first + behind))
    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s

# 测试:
test = 'abcdefg'
s = Solution()
print(s.LeftRotateString(test, 2))
print('-------------------------')
s = Solution1()
print(s.LeftRotateString(test, 2))
