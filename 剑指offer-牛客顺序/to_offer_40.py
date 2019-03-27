# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。'

"""
剑指offer-P276
异或运算
如果一个数组中除一个数字以外都出现两次，则异或以后留下的就是那个只出现一次的数字！

任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。数组中出了两个数字之外，其他数字都出现两次，
那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，那两个不同的数字异或的值不为0，
也就是说这两个数的异或值中至少某一位为1。我们找到结果数字中最右边为1的那一位i，然后依次遍历数组中的数字，
如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。
这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，
然后再对两个组依次进行异或操作，最后每一组得到的结果对应的就是两个只出现一次的数字。
"""

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):  # 异或运算-剑指offer--P276
        # write code here
        if not array or len(array) < 2:
            return
        resultOR = 0
        for i in array:
            resultOR = resultOR ^ i
        index = self.FindFirstBitIs1(resultOR)
        num1, num2 = 0, 0
        for j in array:
            if self.IsBit1(j, index):
                num1 ^= j
            else:
                num2 ^= j
        return [num1, num2]

    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit < 32:
            num = num >> 1
            indexBit += 1
        return indexBit

    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1

# 测试:
aList = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.FindNumsAppearOnce(aList))