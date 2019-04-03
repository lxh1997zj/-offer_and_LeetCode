# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/3 14:20
'''
"""
如果输入中出现了连续（2个及以上）的字母，则认为是分隔符，统计被分隔符split的字母或者字符串的个数。
https://www.nowcoder.com/discuss/172305?type=0&order=0&pos=15&page=0
"""


class Solution:   # 时间O(n), 空间O(n).
    def hhh(self, s):
        if not s or len(s) <= 0:
            return -1
        a = list(s)
        res = []
        if a[0] == a[1]:
            res.append('-')
        else:
            res.append(a[0])
        for i in range(1, len(a)-1):
            if a[i] == a[i-1] or a[i] == a[i+1]:
                res.append('-')
            else:
                res.append(a[i])
        if a[-1] == a[-2]:
            res.append('-')
        else:
            res.append(a[-1])
        # return res
        b = ''.join(res) # return b
        # c = b.split('-') # return c
        # count = 0
        # for j in c:
        #     if j != '':
        #         count += 1
        # return count
        return self.hh(b)

    def hh(self, s):  # 如果不允许split(),就自己写一个函数去查找.
        count = 0
        if s[0] != '-':
            count = 1
        for i in range(1, len(s)):
            if s[i] != '-':
                if s[i - 1] == '-':
                    count += 1
                else:
                    continue
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hhh('aa'))
    print(s.hhh('aab'))
    print(s.hhh('aaaccefgh'))
    print(s.hhh('abbcccadhhh'))
