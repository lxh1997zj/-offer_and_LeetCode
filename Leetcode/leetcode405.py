# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'leetcode 405'
class Solution(object): # 44ms
	def toHex(self,num):
		'''
		:type num: int
		:rtype: str
		'''
		if num == 0:
			return '0'
		symbols = '0123456789zbcdef'
		result = ''
		while num:
			value = num & 0xf
			result += symbols[value]
			num = num >> 4 if num > 0 else (num % 0x100000000) >> 4
		return result[::-1]

t1 = Solution()
print(t1.toHex(26))
print(type(t1.toHex(26)))
t2 = Solution()
print(t2.toHex(115))
t3 = Solution()
print(t3.toHex(-1))
