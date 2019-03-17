# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。'
# 二分查找


class Solution:
    def minNumber(self, rotateArray, index1, index2):
        res = rotateArray[index1]
        for i in range(index1+1, index2+1):
            if res > rotateArray[i]:
                res = rotateArray[i]
        return res
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:   # 方法一
            return None
        if len(rotateArray) == 0:
            return 0
        index1, index2 = 0, len(rotateArray)-1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                return rotateArray[index2]
            indexmid = (index1 + index2) // 2
            if rotateArray[indexmid] == rotateArray[index1] and rotateArray[indexmid] == rotateArray[index2]:
                return self.minNumber(rotateArray, index1, index2)
            if rotateArray[indexmid] >= rotateArray[index1]:
                index1 = indexmid
            if rotateArray[indexmid] <= rotateArray[index2]:
                index2 = indexmid
        return rotateArray[index2]
        """
        left = 0   # 方法二
        right = len(rotateArray)-1
        while left < right:
            mid = int((left+right)/2)
            if rotateArray[mid] > rotateArray[right]:
                left = mid+1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]
        """