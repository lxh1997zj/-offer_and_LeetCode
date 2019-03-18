# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:       # 244ms
    def findDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [0] * (len(nums)+1)
        res = []
        for i in nums:
            a[i] += 1
        for i in range(len(a)):
            if a[i] > 1:
                res.append(i)
        return res
