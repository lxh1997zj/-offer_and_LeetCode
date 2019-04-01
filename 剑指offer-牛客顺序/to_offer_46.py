# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'题目：圆圈中最后剩下的数字'

"""题：0，1，...，n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字."""

"""
解题思路：
约瑟夫环问题，可以根据数学规律找出高效的解法，剑指offer-P302.
公式: f(n, m) = [f(n-1, m) + m] % n  (n > 1)
                0                   (n = 1)
链接2: https://blog.csdn.net/u012505432/article/details/51747181
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        res = 0
        for i in range(2, n+1):  # 这里循环从1和2开始没什么区别
            res = (res + m) % i
        return res


# 测试:
s = Solution()
print(s.LastRemaining_Solution(5, 3))
print(s.LastRemaining_Solution(6, 2))
print(s.LastRemaining_Solution(5, 6))
print(s.LastRemaining_Solution(6, 6))
print(s.LastRemaining_Solution(0, 2))
print(s.LastRemaining_Solution(4000, 997))
print('----------------------------------')


class Solution1:
    def LastRemaining_Solution(self, n, m): # 这个存在语法错误或者数组越界非法访问等情况，通不过oj
        # write code here
        if n < 1 or m < 1:
            return -1
        cnt = 1
        dead = []
        def ans(t, m):
            nonlocal cnt, dead
            for i in range(t):
                if i in dead:
                    continue
                if cnt == m:
                    dead.append(i)
                    cnt = 1
                else:
                    cnt += 1
        while len(dead) < n-1:
            ans(n, m)
        for i in range(n):
            if i not in dead:
                return i


# 测试:
s = Solution1()
print(s.LastRemaining_Solution(5, 3))
print(s.LastRemaining_Solution(6, 2))
print(s.LastRemaining_Solution(5, 6))
print(s.LastRemaining_Solution(6, 6))
print(s.LastRemaining_Solution(0, 2))
# print(s.LastRemaining_Solution(4000, 997)) # 这种情况不能正常输出
