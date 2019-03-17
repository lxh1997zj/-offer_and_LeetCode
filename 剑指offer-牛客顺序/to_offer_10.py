# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？'

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a, b = 1, 2
        for i in range(3, number+1):
            a, b = b, a+b
        return b
"""
这题也是斐波那契数列的改变！
这里其实可以不判断number==2的情况，但是不判断,range要从2开始遍历，即range(2, number);
"""