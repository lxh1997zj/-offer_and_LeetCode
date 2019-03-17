# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.'

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        start, row, col = 0, len(matrix), len(matrix[0])
        res = []
        total = row * col   # 元素个数
        while len(res) < total:
            for i in range(start, col-start): # 向右走
                res.append(matrix[start][i])
            j = -1    # 越界标志
            for j in range(start+1, row-start): # 向下走
                res.append(matrix[j][i])
            if j == -1:
                break
            a = -1
            for a in range(i-1, start-1, -1): # 向左走
                res.append(matrix[j][a])
            if a == -1:
                break
            for b in range(j-1, start, -1): # 向上走
                res.append(matrix[b][a])
            start += 1   # 矩形缩小一圈(一格子)
        return res
"""
total = ((row if row < col else col) - 1) // 2 + 1  # total表示圈数
        while start < total:
"""


"""以下为剑指offer上的方法(P161)"""
class Solution1:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        start, row, col = 0, len(matrix), len(matrix[0])
        res = []
        while row > start * 2 and col > start * 2:
            self.printMatrixRect(matrix, start, row, col, res)
            start += 1
        return res

    def printMatrixRect(self, matrix, start, row, col, res): # 可以直接将两个函数合并成一个函数.
        endX = col - 1 - start
        endY = row - 1 - start
        # 从左到右打印一行:
        for i in range(start, endX+1):
            res.append(matrix[start][i])
        # 从上到下打印一列:
        if endY > start:
            for j in range(start+1, endY+1):
                res.append(matrix[j][endX])
        # 从右到左打印一行:
        if endX > start and endY > start:
            for a in range(endX-1, start-1, -1):
                res.append(matrix[endY][a])
        # 从下到上打印一列:
        if endX > start and endY - 1 > start:
            for b in range(endY-1, start, -1):
                res.append(matrix[b][start])

# 测试:
matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
S.printMatrix(matrix)
S.printMatrix(matrix2)
S.printMatrix(matrix3)
print(S.printMatrix(matrix))
print(S.printMatrix(matrix2))
print(S.printMatrix(matrix3))
S1 = Solution1()
print(S1.printMatrix(matrix))
print(S1.printMatrix(matrix2))
print(S1.printMatrix(matrix3))


class Solution2:  # 利用Python库函数zip的特性
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        return matrix and list(matrix.pop(0))+self.printMatrix(zip(*matrix)[::-1])


class Solution3:        # 类似于反转，模拟魔方逆时针旋转的方法，一直做取出第一行的操作
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat


class Solution4:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res