# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？'


"""
思路:
首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后从前往后依次遍历新字符串，如果遇到空格，就把空格前的字符串用reverse翻转，添加空格，继续遍历。需要注意的是，如果新字符串结尾不是空格，当遍历到结尾的时候，前一个空格到结尾的字符串没有翻转，因此记得跳出遍历后，需要再完成一次翻转操作。
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s or len(s) <= 0:
            return ''
        s = list(s)
        s = self.Reverse(s)
        pStart, pEnd = 0, 0
        result = ''
        listTemp = []
        while pEnd < len(s):
            # 如果字符串长度为1, 直接跳出循环
            # 如果pEnd指针指到最后一个字符, 跳出循环
            if pEnd == len(s) - 1:
                listTemp.append(self.Reverse(s[pStart:]))
                break
            # 这个判断语句位置需要靠前, 用来鉴定字符串开头是否是空格的情况
            elif s[pStart] == ' ':
                pStart += 1
                pEnd += 1
                listTemp.append(' ')
            elif s[pEnd] == ' ':
                listTemp.append(self.Reverse(s[pStart: pEnd]))
                pStart = pEnd
            else:
                pEnd += 1
        for i in listTemp:
            result += ''.join(i)
        return result

    def Reverse(self, s):
        # s是一个list列表
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s


class Solution1:
    def ReverseSentence(self, s): # 利用Python特性.
        # write code here
        new_s = s.split()
        if len(new_s) == 0:
            return s
        return ' '.join(new_s[::-1])


# 测试:
s = Solution()
print(s.ReverseSentence('student. a am I'))
print('----------------------------------')
s = Solution1()
print(s.ReverseSentence('student. a am I'))
