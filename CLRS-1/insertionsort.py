'''
Written:       2018/08/28
Last updated:  2018/08/31
Language: Python

Introduction to Algorithm: I Foundation
'''

#insertion_sort, sort in place
def insertion_sort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A

#pset 2.1-2 reverse insertion-sort
def insertion_sort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A