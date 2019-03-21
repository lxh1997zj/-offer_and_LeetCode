# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)'


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array or len(array) <= 0:
            return 0
        Cursum = 0
        Curgreatsum = array[0]
        for i in range(len(array)):
            if Cursum <= 0:
                Cursum = array[i]
            else:
                Cursum += array[i]
            if Cursum > Curgreatsum:
                Curgreatsum = Cursum
        return Curgreatsum

"""
解法2：动态规划---剑指offer-P220
"""
alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray(alist))