# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def generateMatrix(self, n):  # 44ms
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]  # 螺旋矩阵
        i = 0       # 开始下标
        j = 1       # 记录元素个数
        total = n * n  # 总元素个数
        while j <= total:
            for a in range(i, n-i):  # 向右走
                res[i][a] = j
                j += 1
            b = -1
            for b in range(i+1, n-i):  # 向下走
                res[b][a] = j
                j += 1
            if b == -1:
                break
            c = -1
            for c in range(a-1, i-1, -1):  # 向左走
                res[b][c] = j
                j += 1
            if c == -1:
                break
            for d in range(b-1, i, -1):  # 向上走
                res[d][c] = j
                j += 1
            i += 1   # 圈子减1
        return res

'''
class Solution:   # 最快的解，但是没看懂！
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        max_num = n*n
        output = []
        for i in range(n):
            lists = [0 for i in range(n)]
            output.append(lists)
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for num in range(1, max_num+1):
            if output[r][c] == 0:
                output[r][c] = num
            cr, cc = r+dr[di], c+dc[di]
            if 0<=cr<n and 0<=cc<n and output[cr][cc] == 0:
                r, c = cr, cc
            else:
                di = (di+1)%4
                r, c= r+dr[di], c+dc[di]
        return output
'''