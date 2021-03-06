# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/9 16:20
'''

"""此为错误答案"""

"""
思路:
首先用python的文件读写将示例文件中的xml逐行加入到res列表中，然后定义一个函数(Print_res(res))去打印res列表中的tag, attribute, text,
加入到temp和value两个列表中；通过主函数的一系列操作，列表a是将temp分组后的一个二维列表，a的长度和value的长度相同，
在通过正则表达式匹配找出'<test>', '<second>', '</test>', '</second>'类似的标签，并通过字符串分割舍去 '<', '>', '/'字符，
得到新的两个列表，一个是各个子树的头，另一个是类似于子树结束进入父树分支的下一个结点；
最后通过for循环数组a，来判断a[i][0]是否在两个列表中，print对应的情况。
"""


import re


res = []
with open('example.txt') as f:   # 使用python的文件读写，把每行都加入到res列表中
    for line in f.readlines():
        res.append(line.strip())


def MainCore(res):
    temp, value = Print_res(res)
    # print(temp)
    # print(value)
    a = []
    while len(temp) > 0:
        index_None = temp.index(None)
        b = temp[:index_None]
        if len(b) != 0:
            a.append(b)
        for _ in range(index_None+1):
            temp.pop(0)
    # print(a) # [['test'], ['a1', 'key1', '"google1"', 'key2', '"company1"'], ['name1', 'key1', '"super1"'], ['int1'], ['second'], ['a2', 'key1', '"google2"', 'key2', '"company2"'], ['name2', 'key1', '"super2"'], ['int2'], ['char1']]
    # print(len(a)) # 9

    stack, end = [], []      # 找出'<test>', '<second>', '</test>', '</second>'类似的标签
    for j in range(len(res)-1):
        if re.match('^<[a-zA-Z]+>$', res[j]):  # 正则表达式匹配'<test>'和'<second>'和类似的标签
            stack.append(res[j])
        if re.match('^</[a-zA-Z]+>$', res[j]):  # 正则表达式匹配'</test>'和'</second>'和类似的标签
            end.append(res[j+1])  # 子树完毕后回到父树的分支，类似于这是它的下一个结点
        else:
            continue
    # print(stack, end)  # ['<test>', '<second>'] ['<char1> "c" </char1>']

    new_stack = []
    for q in range(len(stack)):
        p = stack[q].split('<')[1].split('>')[0]   # 提取出标签中的单词
        new_stack.append(p)
    # print(new_stack)    # ['test', 'second']

    new_end = []
    for q in range(len(end)):
        p = end[q].split()[0].split('<')[1].split('>')[0]   # 提取出标签中的单词
        new_end.append(p)
    # print(new_end)   # ['char1']

    j = 0
    for i in range(len(a)):   # 具体输出部分

        # 当a[i][0]在new_end中时，要往回减一个制表符，即从子树回到父树分支:
        if a[i][0] in new_end:
            j -= 1
            if value[i] == None:
                n = (len(a[i]) - 1) // 2
                print('\t'*j + a[i][0] + '-%s:%s'*n % tuple(a[i][1:]))
            elif value[i] != None:
                n = (len(a[i]) - 1) // 2
                if n > 0:
                    print('\t'*j + a[i][0] + '-%s:%s'*n % tuple(a[i][1:]) + '-value:' + value[i])
                else:
                    print('\t'*j + a[i][0] + '-value:' + value[i])

        # 当a[i][0]不在new_stack中时，正常输出:
        elif a[i][0] not in new_stack:
            if value[i] == None:
                n = (len(a[i]) - 1) // 2
                print('\t'*j + a[i][0] + '-%s:%s'*n % tuple(a[i][1:]))
            elif value[i] != None:
                n = (len(a[i]) - 1) // 2
                if n > 0:
                    print('\t'*j + a[i][0] + '-%s:%s'*n % tuple(a[i][1:]) + '-value:' + value[i])
                else:
                    print('\t'*j + a[i][0] + '-value:' + value[i])

        # 当a[i][0]在new_stack中时，制表符加一，即从父树分支进入子树中:
        elif a[i][0] in new_stack:
            if value[i] == None:
                n = (len(a[i]) - 1) // 2
                print('\t'*j + a[i][0] + '-%s:%s' * n % tuple(a[i][1:]))
                j += 1
            elif value[i] != None:
                n = (len(a[i]) - 1) // 2
                if n > 0:
                    print('\t'*j + a[i][0] + '-%s:%s' * n % tuple(a[i][1:]) + '-value:' + value[i])
                    j += 1
                else:
                    print('\t'*j + a[i][0] + '-value:' + value[i])
                    j += 1


def Print_res(res):       # 提取出xml中的tag, attribute, text
    temp, value = [], []
    for i in range(len(res)):
        # 情况1: '', :
        if res[i] == '' or res[i][:2] == '</':
            continue
        # 情况2: <a1   key1="google1" key2="company1"/>
        # 结果temp类似于: temp = ['a1', 'key1', '"google1"', 'key2', '"company1"']
        elif res[i][0] == '<' and res[i][-2:] == '/>':
            s = res[i][1: -2].split()
            for j in range(len(s)):
                if '=' in s[j]:
                    s1 = s[j].split('=')
                    temp += s1
                else:
                    temp.append(s[j])
            temp.append(None)
            value.append(None)
        # 情况3: <name1 key1="super1">"cctv1"</name1>
        # temp = ['name1', 'key1', '"super1"']
        elif res[i].count('<') == 2 and res[i].count('>') == 2:
            a = res[i].split('<')[1].split('>')
            if a[1] != '':
                value.append(a[1].split()[0])
            else:
                value.append(None)
            b = a[0].split()
            for j in range(len(b)):
                if '=' in b[j]:
                    s1 = b[j].split('=')
                    temp += s1
                else:
                    temp.append(b[j])
            temp.append(None)
        # 情况4: '<int1>666', '</int1>', :
        elif res[i][0] == '<' and res[i+1][0:2] == '</':
            a = res[i].split('<')[1].split('>')
            if a[1] != '':
                value.append(a[1].split()[0])
            else:
                value.append(None)
            b = a[0].split()
            for j in range(len(b)):
                if '=' in b[j]:
                    s1 = b[j].split('=')
                    temp += s1
                else:
                    temp.append(b[j])
            temp.append(None)
        # 情况5: '<second>', :
        elif res[i][0] == '<' and res[i+1][0:2] != '</':
            a = res[i].split('<')[1].split('>')
            temp.append(a[0])
            temp.append(None)
            if res[i+1][0] != '<':
                value.append(res[i+1].split()[0])
            else:
                value.append(None)
        else:
            continue
    return temp, value


if __name__ == '__main__':
    MainCore(res)


# 测试结果:
"""
test-value:"main"
	a1-key1:"google1"-key2:"company1"
	name1-key1:"super1"-value:"cctv1"
	int1-value:666
	second
		a2-key1:"google2"-key2:"company2"
		name2-key1:"super2"-value:"cctv2"
		int2-value:777
	char1-value:"c"
"""
