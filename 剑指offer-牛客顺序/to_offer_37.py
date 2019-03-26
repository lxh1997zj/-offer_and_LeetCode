# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'统计一个数字在排序数组中出现的次数。'

"""
思路：二分查找法，分别找到此数字在排序数组中第一次和最后一次出现的位置，然后次数等于两个位置之差加1。
时间复杂度：O(log n)
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.FirstNumber(data, length, k, 0, length-1)
            last = self.LastNumber(data, length, k, 0, length-1)
            if first > -1 and last > -1:
                number = last - first + 1
        return number

    def FirstNumber(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start+end) // 2
        if data[middle] == k:
            if middle > 0 and data[middle-1] == k:
                end = middle - 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.FirstNumber(data, length, k, start, end)

    def LastNumber(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start+end) // 2
        if data[middle] == k:
            if middle < end and data[middle+1] == k:
                start = middle + 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.LastNumber(data, length, k, start, end)

# 测试:
alist = [3, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetNumberOfK(alist, 3))
print(s.GetNumberOfK(alist, 4))
print(s.GetNumberOfK(alist, 5))
