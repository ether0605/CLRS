# coding:utf-8

"""
Written:       2018/08/13
Last updated:  -
Language: Python

binary search
"""
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while (low <= high):
        mid = (low + high)/2
        if item == list[int(mid)]:
            return True
        elif item < list[int(mid)]:
            high = mid - 1
        else:
            low = mid + 1
    return False

assert binary_search([1, 4, 7, 9, 8, 6], 1) == True