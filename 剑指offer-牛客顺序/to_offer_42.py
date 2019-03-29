# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。'

"""
设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，如果和大于目标值，则把后一个指针前移，如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到，就终止操作。
"""

class Solution:  # 使用while循环从两端向中间扫描数组，时间复杂度为O(n)
    def FindNumbersWithSum(self, array, tsum): # 因为是左右指针，所以找到的第一队就是乘积最小的
        # write code here
        if not array or len(array) < 2:
            return []
        beg, end = 0, len(array)-1
        while beg < end:
            sum = array[beg] + array[end]
            if sum == tsum:
                return [array[beg], array[end]]
            elif sum > tsum:
                end -= 1
            else:
                beg += 1
        return []

# 测试:
test = [1, 2, 3, 4, 5, 7, 11, 14, 15]
s = Solution()
print(s.FindNumbersWithSum(test, 16))
print(s.FindNumbersWithSum(test, 17))
print(s.FindNumbersWithSum(test, 23))
