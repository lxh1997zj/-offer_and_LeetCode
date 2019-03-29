# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution():
    def Translate_8_to_az(self, num):  # 输入8进制数，输出对应的26进制字符
        if num < 0:
            return
        c, new_num = 0, 0
        while num > 0:
            a = num % 10
            new_num += a*(8**c)
            c += 1
            num = num // 10
        # print(new_num)
        # new_num = num  # 测试10进制
        temp, res = 0, []
        while new_num > 0:
            b = new_num % 26
            if b == 0:
                b = 26
                new_num -= 1
            res.append(chr(97 + b - 1))
            new_num = new_num // 26
        res.reverse()
        return ''.join(res)

# 测试:
s = Solution()
print(s.Translate_8_to_az(1))
print(s.Translate_8_to_az(32))
print(s.Translate_8_to_az(33))
print(s.Translate_8_to_az(1276))
print(s.Translate_8_to_az(1277))
print(s.Translate_8_to_az(144))
print(s.Translate_8_to_az(150))
# print(s.Translate_8_to_az(26))
# print(s.Translate_8_to_az(702))
# print(s.Translate_8_to_az(703))
# print(s.Translate_8_to_az(100))
# print(s.Translate_8_to_az(104))

print('--------------------------------------')

class Solution1:
    def Translate_az_to_10(self, char):   # 输入26进制字符，输出8进制数
        if not char or len(char) < 0:
            return
        a = list(char)
        res, c = 0, 0
        for i in a[::-1]:
            b = ord(i) - ord('a') + 1
            res += b * (26**c)
            c += 1
        return self.hhh(res)

    def hhh(self, num):
        res = []
        while num > 0:
            a = num % 8
            res.insert(0, str(a))
            num = num // 8
        return ''.join(res)

# 测试:
s1 = Solution1()
print(s1.Translate_az_to_10('a'))
print(s1.Translate_az_to_10('z'))
print(s1.Translate_az_to_10('aa'))
print(s1.Translate_az_to_10('zz'))
print(s1.Translate_az_to_10('aaa'))
print(s1.Translate_az_to_10('cv'))
print(s1.Translate_az_to_10('cz'))
