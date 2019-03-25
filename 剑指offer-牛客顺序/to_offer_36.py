# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'to_offer_35.py的归并解法，调试！'

class Solution2:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 0:
            return 0
        length = len(data)
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        count = self.Core(data, copy, 0, length-1)
        return count % 1000000007

    def Core(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.Core(copy, data, start, start+length)
        right = self.Core(copy, data, start+length+1, end)
        i = start + length
        j = end
        copyindex = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[copyindex] = data[i]
                copyindex -= 1
                i -= 1
                count += j - start - length
            else:
                copy[copyindex] = data[j]
                copyindex -= 1
                j -= 1
        while i >= start:
            copy[copyindex] = data[i]
            copyindex -= 1
            i -= 1
        while j >= start+length+1:
            copy[copyindex] = data[j]
            copyindex -= 1
            j -= 1
        return count + left + right

# 测试:
s = Solution2()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))