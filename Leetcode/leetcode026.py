# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/29 18:10
'''

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

双指针法: 时间复杂度: O(n), 空间复杂度: O(1) 
"""


class Solution:
    def removeDuplicates(self, nums):   # : List[int]) -> int:
        if len(nums) <= 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


# 测试:
s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
