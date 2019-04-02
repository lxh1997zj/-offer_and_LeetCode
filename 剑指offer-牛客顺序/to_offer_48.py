# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。'

"""
剑指offer思路分析：三步走策略：
①只做各位相加不进位（可以用异或来处理，和异或结果相同）
②进位：可以想象为两个数先做位与运算，然后左移一位
③把前两个步骤的结果相加，重复前两步，直到不产生进位为止。在Python中做位运算，需要做越界检查。
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sumN = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1, num2 = sumN, carry
        if num1 < 0x7fffffff:
            return num1
        else:
            return ~(num1 ^ 0xffffffff)


class Solution1:
    def Add(self, num1, num2): # Python自带库函数.
        # write code here
        return sum([num1, num2])


# 通过每次对num1进行与操作保证是一个32位的整形
# 因此最后我们可以判断符号位是否为1做处理
class Solution2:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sumN = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = sumN & 0xffffffff
        return num1 if num1 >> 31 == 0 else num1 - 4294967296


# 测试:
s = Solution()
print(s.Add(16, 14))
print(s.Add(159, 753))
print(s.Add(16, -17))
print('-----------')
s = Solution1()
print(s.Add(16, 14))
print(s.Add(159, 753))
print(s.Add(16, -17))
print('-----------')
s = Solution2()
print(s.Add(16, 14))
print(s.Add(159, 753))
print(s.Add(16, -17))


"""
拓展：不使用新的变量，交换两个变量的值。

1.基于加减法     2.基于异或

a=a+b           a=a^b

b=a-b           b=a^b

a=a-b           a=a^b

(a^b^b=a, a^b^a=b) 自己异或自己等于0, 任何数异或0等于它自身.
"""
