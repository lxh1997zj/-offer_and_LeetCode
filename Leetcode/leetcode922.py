# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def sortArrayByParityII_1(self,A):  # 188ms
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        t = []
        for i in A:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        for x in range(len(A)//2):
            t.append(a[x])
            t.append(b[x])
        return t

    def sortArrayByParityII_2(self,A):  # 180ms
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        result = [0] * n
        even,odd = 0,1
        for i in A:
            if i % 2 == 0:
                result[even] = i
                even += 2
            else:
                result[odd] = i
                odd += 2
        return result
