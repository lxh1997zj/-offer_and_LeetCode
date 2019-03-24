# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。'

class Solution:
    def GetUglyNumber_Solution(self,index):
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

# 测试:
s = Solution()
print(s.GetUglyNumber_Solution(9))
print(s.GetUglyNumber_Solution(10))
print(s.GetUglyNumber_Solution(11))
