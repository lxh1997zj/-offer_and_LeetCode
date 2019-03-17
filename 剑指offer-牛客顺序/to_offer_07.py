# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n <= 39'
# n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)

class Solution:
    def Fibonacci(self, n):  # 循环
        # write code here
        a, b = 0, 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b

class Solution:
    def Fibonacci(self, n):  # 递归，效率低，可能通不过
        # write code here
        a, b = 0, 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


"""
题目拓展1：跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
"""
class Solution1():
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        a, b = 1, 2
        for i in range(2, number):
            a, b = b, a+b
        return b


""" 
题目拓展2：变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# 解题思路：由数学归纳法得规律
class Solution2():
    def jumpFloorII(self, number):
        if number <= 0:
            return 0
        return 2 ** (number-1)


"""
题目拓展3：矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
# 解题思路：这道题本质上还是斐波那契数列问题，注意分析n=0,1,2,3,...的值的情况。
class Solution3():
    def rectCover(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a, b = 1, 2
        for i in range(3, number+1):
            a, b = b, a+b
        return b


# 测试:
s = Solution3()
print(s.rectCover(10))
print(s.rectCover(4))
print(s.rectCover(5))
print(s.rectCover(6))

