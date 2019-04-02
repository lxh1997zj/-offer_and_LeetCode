# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。'


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):   # 先排序，然后遍历数组，时间复杂度O(nlogn)
        # write code here
        if not numbers or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers)-1:
                return False
        numbers.sort()
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i+1]:
                duplication[0] = numbers[i]
                # print(duplication[0])
                return True
        return False


class Solution1:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):   # 使用辅助空间:哈希表。时间复杂度为O(n)，空间复杂度为O(n)
        # write code here
        if not numbers or len(numbers) <= 1:
            return False
        useDic = set()
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers)-1:
                return False
            if numbers[i] not in useDic:
                useDic.add(numbers[i])
            else:
                duplication[0] = numbers[i]
                return True
        return False


"""
解题思路三：
重排数组：
从头到尾扫描数组的每个数字，当扫描到下标为i的数字时，首先比较这个数字（假设为m）是否等于i,如果是，接着扫描下一个数字；如果不是，那么再将它和下标为m的数字对比，如果两者不相等，就把它和第m个数字交换，把m放到属于它的位置，如果两者相等，那么就找到了一个重复的数字。重复这个过程，知道发现一个重复的数字。

解题代码：
(根据代码分析复杂度：所有操作都在输入数组上进行，不需要额外分配空间，因此空间复杂度为O(1);尽管代码中有一个两重循环，但是每个数字最多只要交换两次就能找到它自己的位置，因为总的时间复杂度为O(n))
"""


class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):  # 空间复杂度O(1),时间复杂度O(n)
        # write code here
        if not numbers or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers)-1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[i]
                    # numbers[i] = numbers[temp]
                    # numbers[temp] = temp
                    numbers[i], numbers[temp] = numbers[temp], numbers[i]
        return False


# 测试:
s = Solution()
print(s.duplicate([2, 3, 1, 0, 2, 5, 3], [1]))
print(s.duplicate([2, 1, 3, 0, 4], [1]))
print('-------------------------------------')
s = Solution1()
print(s.duplicate([2, 3, 1, 0, 2, 5, 3], [1]))
print(s.duplicate([2, 1, 3, 0, 4], [1]))
print('-------------------------------------')
s = Solution2()
print(s.duplicate([2, 3, 1, 0, 2, 5, 3], [1]))
print(s.duplicate([2, 1, 3, 0, 4], [1]))
print('-------------------------------------')
