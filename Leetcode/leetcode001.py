# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/10 17:34
'''

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution(object):
    def twoSum(self, nums, target):  # 首尾递进查找做的，需要一次排序，时间复杂度是 O(nlogn), 再去查找原来位置的索引
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        news = sorted(range(len(nums)), key=lambda k: nums[k])
        i = 0
        j = len(news) - 1
        while i != j:
            sum_result = nums[news[i]] + nums[news[j]]
            if sum_result == target:
                return [news[i], news[j]]
            elif sum_result > target:
                j -= 1
            else:
                i += 1
        return []


class Solution1(object):
    def twoSum(self, nums, target):  # 利用hashMap来判断是否已存在目标元素，若没有则插入当前元素
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashMap:
                return [hashMap[another_num], index]
            hashMap[num] = index
        return None


# 测试:
s = Solution()
print(s.twoSum([2,7, 15 ,8], 9))
print(s.twoSum([3, 2, 4], 6))
print('-----------------------------')
s = Solution1()
print(s.twoSum([2,7, 15 ,8], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([0, 2, 3, 4], 4))
