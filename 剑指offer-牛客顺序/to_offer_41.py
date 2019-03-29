# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输出所有和为S的连续正数序列'

"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""

"""
设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，如果和大于目标值，则从当前和中删除small值，
并把small值加一，如果和小于目标值，则把big值加一，再把新的big值加入和中。如果和等于目标值，就输出small到big的序列，
同时把big加一并加入和中，继续之前的操作。
"""

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) // 2
        cursum = small + big
        res = []
        while small < middle:
            if cursum == tsum:
                res.append(list(range(small, big+1)))
            while cursum > tsum and small < middle:
                cursum -= small
                small += 1
                if cursum == tsum:
                    res.append(list(range(small, big+1)))
            big += 1
            cursum += big
        return res


class Solution1:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        beg, end = 1, 2
        middle = (tsum + 1) >> 1
        curSum = beg + end
        res = []
        while beg < middle:
            if curSum == tsum:
                res.append(list(range(beg, end+1)))
                end += 1
                curSum += end
            elif curSum < tsum:
                end += 1
                curSum += end
            else:
                curSum -= beg
                beg += 1
        return res


# 测试:
s = Solution()
print(s.FindContinuousSequence(15))
print('--------------------------')
s = Solution1()
print(s.FindContinuousSequence(15))
