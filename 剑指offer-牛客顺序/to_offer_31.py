# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。'

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):  # 直接累加
        # write code here
        total = 0
        for i in range(1, n+1):
            total += self.SingleNumberhas1(i)
        return total

    def SingleNumberhas1(self, number):
        count = 0
        while number:
            if number % 10 == 1:
                count += 1
            number = number // 10
        return count


class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):  # 先转换成字符串形式
        # write code here
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count


class Solution2:
    def NumberOf1Between1AndN_Solution(self, n):  # python自带库函数count()
        # write code here
        Count = 0
        for i in range(1, n+1):
            Count += str(i).count('1')
        return Count


"""
参考链接:  时间复杂度O(logn)
https://blog.csdn.net/yi_Afly/article/details/52012593
"""
class Solution3:
    def NumberOf1Between1AndN_Solution(self, n):  # 找规律,时间复杂度O(logn)
        # write code here
        if n < 1:
            return 0
        count, base, round = 0, 1, n
        while round:
            weight = round % 10
            round = round // 10
            count += round*base
            if weight == 1:
                count += n % base + 1
            if weight > 1:
                count += base
            base *= 10
        return count

# 测试:
s = Solution()
print(s.NumberOf1Between1AndN_Solution(534))
print('------------------------------------')
s = Solution1()
print(s.NumberOf1Between1AndN_Solution(530))
print('------------------------------------')
s = Solution2()
print(s.NumberOf1Between1AndN_Solution(504))
print('------------------------------------')
s3 = Solution3()
print(s3.NumberOf1Between1AndN_Solution(534))
print(s3.NumberOf1Between1AndN_Solution(530))
print(s3.NumberOf1Between1AndN_Solution(504))
print(s3.NumberOf1Between1AndN_Solution(514))
print(s3.NumberOf1Between1AndN_Solution(10))
print(s3.NumberOf1Between1AndN_Solution(1))
print(s3.NumberOf1Between1AndN_Solution(0))