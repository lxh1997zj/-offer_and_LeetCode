# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import heapq

def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

"""
result:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""