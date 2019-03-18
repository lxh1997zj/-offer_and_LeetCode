# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:

    def spiralOrder(self, matrix):   # 44ms
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        cow = len(matrix)  # 行号
        col = len(matrix[0]) if cow else 0  # 列号
        total = cow * col   # 元素个数
        res = []
        if matrix == []:
            return res
        i = 0
        while len(res) < total:
            for a in range(i, col - i):  # 向右走
                res.append(matrix[i][a])
            b = -1
            for b in range(i + 1, cow - i):  # 向下走
                res.append(matrix[b][a])
            if b == -1:
                break
            c = -1
            for c in range(a - 1, i - 1, -1):  # 向左走
                res.append(matrix[b][c])
            if c == -1:
                break
            for d in range(b - 1, i, -1):   # 向上走
                res.append(matrix[d][c])
            i += 1   # 圈子缩小一格
        return res

    '''
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = 0
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                    di, dj = dj, -di
                i += di
                j += dj
        return r
    '''
    '''
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 取首行，去除首行后，对矩阵翻转来创建新的矩阵
        # 再递归直到新矩阵为[],退出并将取到的数据返回
        ret = []
        if matrix == []:
            return ret
        ret.extend(matrix[0])
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return ret
        r = self.spiralOrder([i for i in zip(*new)])
        ret.extend(r)
        return ret
    '''