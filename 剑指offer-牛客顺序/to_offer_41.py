# !/usr/bin/env python3
# -*- coding:utf-8 -*-

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
