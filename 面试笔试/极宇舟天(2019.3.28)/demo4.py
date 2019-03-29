# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'极宇舟天笔试题(2019.3.28)'

"""
给出一个区间的集合，请合并所有重叠的区间。(leetcode056)
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x.start)
        res = []
        for interval in intervals:
            if not res or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        temp = []
        for i in res:
            temp.append([i.start, i.end])
        return temp
# 测试:
# [[2, 3], [1, 2], [4, 7], [4, 5], [7, 9]]
# a = Interval(2, 3)
# b = Interval(1, 2)
# c = Interval(4, 7)
# d = Interval(4, 5)
# e = Interval(7, 9)

a = Interval(1, 3)
b = Interval(2, 6)
c = Interval(8, 10)
d = Interval(15, 18)

S = Solution()
print(S.merge([a,b,c,d,]))
