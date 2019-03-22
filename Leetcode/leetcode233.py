# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        count, base, round = 0, 1, n
        while round:
            weight = round % 10
            round = round // 10
            count += round*base
            if weight == 1:
                count += n % base + 1
            if weight > 1:
                count += base
            base *= 10
        return count

s = Solution()
print(s.countDigitOne(13))
