# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。'

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and self.Sum_Solution(n-1) + n  # 终止递归采用逻辑与的短路特性


class Solution1:
    def Sum_Solution(self, n):
        return sum(list(range(1, n+1)))   # Python自带的sum函数


"""
思路二：利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反运算，
那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。
"""


class Solution2:
    def Sum_Solution(self, n):
        return self.sumN(n)

    def sum0(self, n):
        return 0

    # 利用非0值作两次非运算返回false, 0作两次非运算返回True
    def sumN(self, n):
        func = {False: self.sum0, True: self.sumN}
        # 此处的fun[not not n] 不能写作func[not not n-1], 否则测试用例为0的话, 就会无限次迭代
        return n + func[not not n](n - 1)


# 测试:
s = Solution()
print(s.Sum_Solution(5))
print(s.Sum_Solution(0))
print('---------------')
s = Solution1()
print(s.Sum_Solution(5))
print(s.Sum_Solution(0))
print('---------------')
s = Solution2()
print(s.Sum_Solution(5))
print(s.Sum_Solution(0))
