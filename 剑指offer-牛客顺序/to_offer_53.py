# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 19:17
'''

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

"""
考虑是否有e存在，如果有，e后面必须有数字，且必须是整数（正整数o或负整数），如果没有e存在，则判断它是不是普通的数字。
"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) <= 0:
            return False
        res = [i.lower() for i in s]
        if 'e' in res:
            index = res.index('e')
            front = res[: index]
            behind = res[index+1:]
            if '.' in behind or len(behind) == 0:
                return False
            isFront = self.isDigit(front)
            isBehind = self.isDigit(behind)
            return isFront and isBehind
        else:
            return self.isDigit(res)

    def isDigit(self, a_list):
        num = 0
        stdNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        for i in range(len(a_list)):
            if a_list[i] not in stdNum:
                return False
            if a_list[i] == '.':
                num += 1
            if a_list[i] in '+-' and i != 0:
                return False
        if num > 1:
            return False
        return True


class Solution1:  # python自带特性:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            if float(s):
                return True
        except:
            return False


# 测试:
s = Solution()
print(s.isNumeric('+100'))
print(s.isNumeric('5e2'))
print(s.isNumeric('-123'))
print(s.isNumeric('3.1415926'))
print(s.isNumeric('-1E-16'))
print('------------------------')
print(s.isNumeric('12e'))
print(s.isNumeric('1a3.14'))
print(s.isNumeric('1.2.3'))
print(s.isNumeric('+-5'))
print(s.isNumeric('12e+4.3'))
print('-------------------------')
print(s.isNumeric('1.2e3'))
print('============================')
s = Solution1()
print(s.isNumeric('+100'))
print(s.isNumeric('5e2'))
print(s.isNumeric('-123'))
print(s.isNumeric('3.1415926'))
print(s.isNumeric('-1E-16'))
print('------------------------')
print(s.isNumeric('12e'))
print(s.isNumeric('1a3.14'))
print(s.isNumeric('1.2.3'))
print(s.isNumeric('+-5'))
print(s.isNumeric('12e+4.3'))
print('-------------------------')
print(s.isNumeric('1.2e3'))
