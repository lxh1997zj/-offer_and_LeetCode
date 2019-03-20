# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。'

"""
解题思路：根据数组特点找出时间复杂度为O(n)的算法。因为该数字出现次数比其他所有数字出现的次数之和还要多，所有要找的数字肯定是最后一次把次数设为1时对应的数字。
"""

"""
根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值：数组中的一个数字以及它出现的次数，
然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，当次数等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，
直到进行到最后，然后再验证最后留下的数字是否出现次数超过一半，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 检查数组是否为无效输入
        if not numbers or len(numbers) <= 0:
            return 0
        res = numbers[0]
        temp = 1
        # 若存在则该数出现次数比其他所有数字出现次数之和还要多，则要找的数字肯定是最后一次把次数设为1时对应的数字
        for i in range(1, len(numbers)):
            if temp == 0:
                res = numbers[i]
                temp = 1
            elif numbers[i] == res:
                temp += 1
            else:
                temp -= 1

        # 检查其次数是否大于数组的一半，若不是则返回0
        def IsMoreThanHalfNum(numbers, number):
            temp = 0
            for i in range(len(numbers)):
                if numbers[i] == number:
                    temp += 1
            if temp*2 <= len(numbers):
                return False
            return True
        if IsMoreThanHalfNum(numbers, res):
            return res
        return 0
        """
        sum = 0  # 第二个函数可以简写成以下这种形式，拿数去比较！
        for j in numbers:
            if j == res:
                sum += 1
        return res if sum*2 > len(numbers) else 0
        """
"""
方法二：类似于快排，出现次数最多的数，必然是数组中间的数。
https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.py
"""