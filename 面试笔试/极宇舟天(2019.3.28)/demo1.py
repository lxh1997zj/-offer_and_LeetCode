# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'极宇舟天笔试题(2019.3.28)'

"""
请找出数组中的某个数，它的左侧数字相加之和等于右边
https://my.oschina.net/fengcunhan/blog/214508
"""

class Solution():
    def FndIndex(self, array):
        if not array or len(array) <= 0:
            return
        length = len(array)
        beg, end = 0, length-1
        index = length // 2
        total = sum(array)
        while index > beg and index < end:
            totalLeft = 0
            for i in array[:index]:
                totalLeft += i
            doubleValue = total - array[index]
            if totalLeft * 2 < doubleValue:
                beg = index
                index = index + (length - index) // 2
            elif totalLeft *2 > doubleValue:
                end = index
                index = beg + (index - beg) // 2
            else:
                return index
        return None

# 测试:
s = Solution()
print(s.FndIndex([6, 2, 4, 5, 3]))
print(s.FndIndex([12, 2, 4, 5, 3]))
print(s.FndIndex([6, 2, 4, 5, 12]))
print(s.FndIndex([6, 2, 4, 5, 4]))
print(s.FndIndex([1]))
print(s.FndIndex([]))
