# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'比较a, b, c, d的大小,赋值给min'

class Solution:
    def Compare(self, a, b, c, d):
        res = []
        res.append(a)
        res.append(b)
        res.append(c)
        res.append(d)
        min = res[0]
        for i in range(1, len(res)):
            if res[i] < min:
                min = res[i]
        return min

# 测试:
s = Solution()
print(s.Compare(3, 5, 9, 1))
