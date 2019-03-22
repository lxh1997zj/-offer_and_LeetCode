# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。'

"""cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。"""
from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return ''
        strList = []
        for i in numbers:
            strList.append(str(i))
        # key是一种比较规则
        # 比较 x+y 和 x-y 的大小, 因为为str型, 需要先转换成int型
        key = cmp_to_key(lambda x, y: int(x+y)-int(y+x))
        strList.sort(key=key)
        return ''.join(strList)

numbers = [3, 32, 321]
s = Solution()
print(s.PrintMinNumber(numbers))


class Solution1:
    def PrintMinNumber(self, numbers):  # 冒泡排序
        # write code here
        if len(numbers)<=0:
            return ""
        reslist = [str(i) for i in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if reslist[i] +reslist[j] > reslist[j] + reslist[i]:
                    reslist[i], reslist[j] = reslist[j], reslist[i]
        return ''.join(reslist)

numbers = [3, 32, 321]
s = Solution1()
print(s.PrintMinNumber(numbers))