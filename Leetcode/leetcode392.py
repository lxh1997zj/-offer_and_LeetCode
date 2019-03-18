# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'给定字符串 s 和 t ，判断 s 是否为 t 的子序列。'
# 自己做的
class Solution:    # 376ms 
	def isSubsequence(self,s,t):
		i = 0
		j = 0
		while i < len(s) and j < len(t):
			"""
            :type s: str
            :type t: str
            :rtype: bool
            """
			if s[i] == t[j]:
				i += 1
			j += 1
		if i == len(s):
			return True
		else:
			return False


# 优质答案:
class Solution:    # 44ms
	def isSubsequence(self,s,t):
		j = 0   # j表示t的当前的index,从0出开始搜索
		for i in range(len(s)): # 依据s进行搜索
			temp = s[i]  # 当前需要搜索的字符为temp 
			try:
				res = t.index(temp,j)
			except ValueError:   # 如果没找到返回错误
				return False
			else:   # 找到了
				j = res + 1  # 从j的下一个搜索开始
		# for循环结束,说明全部找到了
		return True

'''
index()用法:
str.index(str, beg=0, end=len(string))
str--指定检索的字符串
beg--开始索引,默认为0
end--结束索引,默认为字符串的长度
如果包含子字符串返回开始的索引值,否则抛出异常。
'''