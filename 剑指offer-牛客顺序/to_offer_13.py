# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。'

class Solution:
    def reOrderArray(self, array):  # 时间复杂度O(n)空间复杂度O(n)，开劈新数组
        # write code here
        res1, res2 = [], []
        for i in array:
            if i%2 == 1:
                res1.append(i)
            else:
                res2.append(i)
        return res1 + res2

# 也可以用冒泡排序来写，时间复杂度O(n2)

"""
拓展：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

解题思路：使用两个指针，第一个指针初始化指向数组的第一个数字，从前向后移动，遇到偶数就停下来；第二个指针指向数组的最后一个数字，从后向前移动，遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。
"""
class Solution1:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return
        if len(array) == 1:
            return array
        left, right = 0, len(array)-1
        while left < right:
            while array[left] % 2 == 1:
                left += 1
            while array[right] % 2 == 0:
                right -= 1
            if left < right:
                array[left], array[right] = array[right], array[left]
            # array[left], array[right] = array[right], array[left]
            # left += 1
            # right -= 1
        #array[left], array[right] = array[right], array[left]
        return array
s = Solution1()
print(s.reOrderArray([1,2,3,4,5,6,7,8]))
print(s.reOrderArray([1,3,3,4,10,5,3,6,6,7]))

class Solution3():
# 可扩展性的解法
# 注意在一个函数的输入中, 输入另一个函数的写法func = self.fucName, funcName不需要加括号
    def Reorder(self, pData, length, func):
        if length == 0:
            return

        pBegin = 0
        pEnd = length - 1

        while pBegin < pEnd:
            while pBegin < pEnd and not func(pData[pBegin]):
                pBegin += 1
            while pBegin < pEnd and func(pData[pEnd]):
                pEnd -= 1

            if pBegin < pEnd:
                pData[pBegin], pData[pEnd] = pData[pEnd], pData[pBegin]
        return pData


    def isEven(self, n):
        return not n & 0x1


    def isNegtive(self, n):
        return n >= 0


    def ReorderOddEven(self, pData):
        length = len(pData)
        return self.Reorder(pData, length, func=self.isNegtive)
S = Solution3()
print(S.ReorderOddEven([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))