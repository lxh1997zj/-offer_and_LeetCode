# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
"""


"""
先置换特殊字符AJQK为数字，排序，然后求出大小王即0的个数，然后求出除去0之外的，数组间的数字间隔(求间隔的时候记得减去1，比如4和5的间隔为5-4-1，表示4和5是连续的数字)，同时求间隔的时候需要鉴别是否出现对。最后比较0的个数和间隔的大小即可。
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        zeros = numbers.count(0)
        for key, value in enumerate(numbers[:-1]):
            if value != 0:
                if value == numbers[key+1]:
                    return False
                zeros = zeros - (numbers[key+1] - value - 1)
                if zeros < 0:
                    return False
        return True


# 测试:
test = [1, 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print(s.IsContinuous(test))
print(s.IsContinuous(test2))
print('-------------------')


class Solution1:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return False
        # 把A, J, Q, K转换一下
        transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]
        numbers.sort()
        numberOfzero, numberOfgap = 0, 0
        # 计算0的个数:
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numberOfzero += 1
            i += 1
        # 计算间隔的个数:
        small = numberOfzero
        big = small + 1
        while big < len(numbers):
            # 如果有对子，则不可能是顺子
            if numbers[small] == numbers[big]:
                return False
            numberOfgap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfzero < numberOfgap else True


# 测试:
test3 = ['A', 3, 2, 5, 0]
test4 = [0, 3, 1, 6, 4]
s = Solution1()
print(s.IsContinuous(test3))
print(s.IsContinuous(test4))
