# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""冒泡排序"""

def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [1,2,5,4,3,6,9,8,7]
print(bubble_sort(array))