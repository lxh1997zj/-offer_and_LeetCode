# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'极宇舟天笔试题(2019.3.28)'

"""
链接：https://www.nowcoder.com/questionTerminal/cbe2c7568ada448c8308dea259f102ba
来源：牛客网
银行取款排队模拟 
假设银行有4个柜台，假设某天有200位客户来办理业务，每个客户到达银行的时间和业务处理时间分别用两个数组arrive_time 和 process_time 来描述。 
请写程序计算所有客户的平均等待时间，假设每个客户在去到营业部之后先拿号排队，然后在任意一个柜台有空闲的时候，号码数最小的客户上去办理，
假设所有的客户拿到号码之后不会因为银行众所周知的慢而失去耐心走掉。
"""


class Solution():
    def hhhh(self, arrive_array, process_array):  # 优先队列
        import queue
        que = queue.PriorityQueue()
        for i in range(4):
            que.put(arrive_array[i] + process_array[i])

        totalwaittime = 0
        for i in range(4, len(arrive_array)):
            waittime = que.get() - arrive_array[i]
            # 负数不需要等待
            waittime = max(waittime, 0)
            totalwaittime += waittime
            que.put(waittime + arrive_array[i] + process_array[i])
        return totalwaittime * 1.0 / len(arrive_array)

# 测试:
a = [1, 2, 3, 4, 4, 8]
b = [50, 20, 11, 25, 30, 40]
a1 = [10, 12, 15, 17, 18, 19, 19, 20, 25]
b1 = [1, 18, 10, 19, 16, 8, 6, 7, 3]
s = Solution()
print(s.hhhh(a, b))
print(s.hhhh(a1, b1))


class Solution1():
    def hhhh(self, arrive_array, process_array):   # 先求四个柜台的最先完成的个体
        PriorityQueue = []
        for i in range(4):
            PriorityQueue.append(arrive_array[i] + process_array[i])
        totalwaittime = 0
        for i in range(4, len(arrive_array)):
            temp = 0
            for j in range(len(PriorityQueue)):
                if PriorityQueue[j] == min(PriorityQueue):
                    temp = j
            waittime = min(PriorityQueue) - arrive_array[i]
            # 负数不需要等待
            waittime = max(waittime, 0)
            totalwaittime += waittime
            PriorityQueue.pop(temp)
            PriorityQueue.append(waittime + arrive_array[i] + process_array[i])
        return totalwaittime * 1.0 / len(arrive_array)

# 测试:
a2 = [10, 12, 15, 17, 18, 19, 19, 20, 25]
b2 = [1, 18, 10, 19, 16, 8, 6, 7, 3]
a3 = [1, 2, 3, 4, 4, 8]
b3 = [50, 20, 11, 25, 30, 40]
s = Solution1()
print(s.hhhh(a2, b2))
print(s.hhhh(a3, b3))
