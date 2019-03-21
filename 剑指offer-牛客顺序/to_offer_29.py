# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。'

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):  # 先用快排排序数组，然后直接按数组特性取出前K个数[:k]
        # write code here
        if not tinput or k > len(tinput):
            return []
        def quick_sort(array, beg, end):
            if beg > end:
                return
            piovt = array[beg]
            left, right = beg, end
            while left < right:
                while left < right and array[right] >= piovt:
                    right -= 1
                array[left] = array[right]
                while left < right and array[left] <= piovt:
                    left += 1
                array[right] = array[left]
            array[right] = piovt
            quick_sort(array, beg, right-1)
            quick_sort(array, right+1, end)
            return array
        return quick_sort(tinput, 0, len(tinput)-1)[:k]


class Solution1():
    def GetLeastNumbers_Solution(self, tinput, k):  # Python自带的sort函数先排序在取数
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]


class Solution2():
    def GetLeastNumbers_Solution(self, tinput, k):  # 堆排序
        import heapq
        if not tinput or k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)



"""
可以适用于海量数据的方法，该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。
"""
class Solution3():
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        import heapq
        output = []
        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]


# 测试:
tinput = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers_Solution(tinput, 5))
print('-----------------------------------')
s1 = Solution1()
print(s1.GetLeastNumbers_Solution(tinput, 4))
print(s1.GetLeastNumbers_Solution(tinput, 4))
print(s1.GetLeastNumbers_Solution(tinput, 5))
print('-----------------------------------')
s2 = Solution2()
print(s2.GetLeastNumbers_Solution(tinput, 4))
print(s2.GetLeastNumbers_Solution(tinput, 4))
print(s2.GetLeastNumbers_Solution(tinput, 5))
print('-----------------------------------')
s3 = Solution3()
print(s3.GetLeastNumbers_Solution(tinput, 4))
print(s3.GetLeastNumbers_Solution(tinput, 4))
print(s3.GetLeastNumbers_Solution(tinput, 5))