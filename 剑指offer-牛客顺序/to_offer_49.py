# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。'

class Solution:
    def StrToInt(self, s):  # 考虑特殊情况.
        # write code here
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sum = 0
        label = 1
        for i in range(len(s)):
            if i == 0:
                if s[i] == '-':
                    label = -1
                    continue
                elif s[i] == '+':
                    continue
            if s[i] in numbers:
                sum = sum * 10 + numbers.index(s[i])
            else:
                sum = 0
                break
        return sum * label


class Solution1:
    def StrToInt(self, s):  # python自带库int().
        # write code here
        try:
            return int(s)
        except:
            return 0


# 测试:
s = Solution()
print(s.StrToInt('12345'))
print(s.StrToInt('-12345'))
print(s.StrToInt('+12345'))
print(s.StrToInt('012345'))
print(s.StrToInt('1234abc'))
print(s.StrToInt('0'))
print(s.StrToInt('-123-56'))
print('---------------------')
s = Solution1()
print(s.StrToInt('12345'))
print(s.StrToInt('-12345'))
print(s.StrToInt('+12345'))
print(s.StrToInt('012345'))
print(s.StrToInt('1234abc'))
print(s.StrToInt('0'))
print(s.StrToInt('-123-56'))
