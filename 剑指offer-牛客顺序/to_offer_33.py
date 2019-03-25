# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。'

"""
空间换时间。建立一个长度为n的数组，保存这n个丑数。在进行运算的时候，某个位置需要求得丑数一定是前面某个丑数乘以2、3或者5的结果，我们分别记录之前乘以2后能得到的最大丑数M2，乘以3后能得到的最大丑数M3，乘以5后能得到的最大丑数M5，那么下一个丑数一定是M2，M3，M5中的最小的那一个。同时注意到，已有的丑数是按顺序存放在数组中的。对乘以2而言，肯定存在某一个丑数T2，排在他之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，在他之后的每一个丑数乘以2得到的结果都会太大，我们只需记下这个丑数的位置，每次生成新的丑数的时候，去更新这个T2。对于3和5同理。
"""

class Solution:
    def GetUglyNumber_Solution(self,index):   # 以时间换空间
        if index <= 0:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextindex = 1
        while nextindex < index:
            minval = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(minval)
            while res[t2]*2 <= minval:
                t2 += 1
            while res[t3]*3 <= minval:
                t3 += 1
            while res[t5]*5 <= minval:
                t5 += 1
            nextindex += 1
        return res[index-1]


class Solution1:
    def GetUglyNumber_Solution(self, index):  # 对每个数都进行判断是不是丑数！时间效率很低，牛客上通不过！
        # write code here
        if index <= 0:
            return 0
        number, uglycount = 0, 0
        while uglycount < index:
            number += 1
            if self.Isugly(number):
                uglycount += 1
        return number

    def Isugly(self, number):
        while number % 2 == 0:
            number //= 2
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5
        return True if number == 1 else False


# 测试:
s = Solution()
print(s.GetUglyNumber_Solution(9))
print(s.GetUglyNumber_Solution(10))
print(s.GetUglyNumber_Solution(11))
print('---------------------------')
s = Solution1()
print(s.GetUglyNumber_Solution(9))
print(s.GetUglyNumber_Solution(10))
print(s.GetUglyNumber_Solution(11))