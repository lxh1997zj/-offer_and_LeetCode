# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 快排1:
def quick_sort(array, i, j):
    if i > j:
        return
    left, right = i, j
    temp = array[i]
    while left < right:
        while left < right and array[right] >= temp:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= temp:
            left += 1
        array[right] = array[left]
    array[right] = temp
    quick_sort(array, i, right-1)
    quick_sort(array, right+1, j)

if __name__ == '__main__':
    array = [7,6]
    quick_sort(array, 0, len(array)-1)
    print(array)
    array1 = [6,7]
    quick_sort(array1, 0, len(array1) - 1)
    print(array1)

print('-------------------------------------')

# 快排2:
def partition(array, beg, end):
    if beg > end:
        return
    index = beg
    piovt = array[index]
    left, right = beg+1, end
    while True:
        while left <= right and array[right] >= piovt:
            right -= 1
        while left <= right and array[left] < piovt:
            left += 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[right], array[index] = piovt, array[right]
    return right
def quick_sort(array, i, j):
    if i < j:
        index_piovt = partition(array, i, j)
        quick_sort(array, i, index_piovt-1)
        quick_sort(array, index_piovt+1, j)
if __name__ == '__main__':
    # array = [6,1,2,7,9,3,4,5,10,8]
    array = [7,6]
    print(partition(array, 0, len(array)-1))
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)

print('-------------------------------------')

# 快排3:
def quick_sort3(array):
    if not array:
        return []
    piovt = array[0]
    left = quick_sort3([x for x in array[1:] if x < piovt])
    right = quick_sort3([x for x in array[1:] if x >= piovt])
    return left + [piovt] + right

if __name__ == '__main__':
    array = [6,1,2,7,9,3,4,5,10,8]
    array3 = [7,6]
    print(quick_sort3(array))
    quick_sort3(array3)
    print(array3)


"""
# result:
[6, 7]
[6, 7]
-------------------------------------
1
[6, 7]
[6, 7]
-------------------------------------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[7, 6]
"""