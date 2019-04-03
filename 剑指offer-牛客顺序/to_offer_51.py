# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/1 20:50
'''

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""

"""
作图画出一个n*n的矩阵，即可看出规律。注意需要得到的向量初始化的时候，初始化的值应该为1。
"""


class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [1] * n
        C = [1] * n
        D = [1] * n
        for i in range(1, n):
            C[i] = C[i-1] * A[i-1]
        for j in range(n-2, -1, -1):
            D[j] = D[j+1] * A[j+1]
        for k in range(0, n):
            B[k] = C[k] * D[k]
        return B


class Solution1:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for j in range(len(A)-2, -1, -1):
            temp *= A[j+1]
            B[j] *= temp
        return B


# 测试:
s = Solution()
print(s.multiply([1, 2, 3, 4, 5]))
print('-------------------------')
s = Solution1()
print(s.multiply([1, 2, 3, 4, 5]))
