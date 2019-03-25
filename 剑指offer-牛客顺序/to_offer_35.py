# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007'

class Solution:
    def InversePairs(self, data): # 运行超时:您的程序未能在规定时间内运行结束,请检查是否循环有错或算法复杂度过大,case通过率为50.00%
        # write code here
        if len(data) <= 0:
            return 0
        count, copylist = 0, []
        for i in range(len(data)):
            copylist.append(data[i])
        copylist.sort()
        i = 0
        while len(copylist) > i:
            count += data.index(copylist[i])
            data.remove(copylist[i])
            i += 1
        return count % 1000000007


class Solution1:
    def InversePairs(self, data):  # case通过率为25.00%
        # write code here
        if len(data) <= 0:
            return 0
        count = 0
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                if data[i] > data[j]:
                    count += 1
        return count % 1000000007


class Solution2:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 0:
            return 0
        length = len(data)
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        # copy数组为原数组data的复制,在后面充当辅助数组
        count = self.Core(data, copy, 0, length-1)
        return count % 1000000007

    def Core(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2   # length为划分后子数组的长度
        left = self.Core(copy, data, start, start+length)
        right = self.Core(copy, data, start+length+1, end)
        # 初始化i为前半段最后一个数字的下标
        i = start + length
        # 初始化j为后半段最后一个数字的下标
        j = end
        # indexCopy为辅助数组的指针，初始化其指向最后一位
        copyindex = end
        count = 0
        # 对两个数组进行对比取值的操作：
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
        # 剩下一个数组未取完的操作：
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
s = Solution()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
print('--------------------------------------')
s = Solution1()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
print('--------------------------------------')
s = Solution2()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))