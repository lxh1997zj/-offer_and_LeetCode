# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:      # 44ms
    def merge(self,nums1,m,nums2,n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()