# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/7 16:44
'''
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""


class Solution:            # 直接求排序后的中位数
    def __init__(self):
        self.array = []
    def Insert(self, num):
        # write code here
        self.array.append(num)
        self.array.sort()
    def GetMedian(self, M):
        # write code here
        length = len(self.array)
        if len(self.array) % 2 == 1:
            return self.array[length // 2]
        else:
            return (self.array[length//2 - 1] + self.array[length//2]) / 2.0


class Solution1:             # 构建最大堆最小堆
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0
    def Insert(self, num):
        if num & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self):
        pass
