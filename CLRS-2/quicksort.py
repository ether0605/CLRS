'''
Written:       2018/08/31
Last updated:  2018/09/03
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics
'''

#quicksort
import random
class quick_sort(A):
    def quicksort(A, p, r):
    # recursive call on quicksort
        if p < r:
            q = partition(A, p, r)
            quicksort(A, p, q-1)
            quicksort(A, q+1, r)

    def partition(A, p, r):
    # rearrange the subarray in place
        pivot = A[r]
        i = p-1
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def ram_partition(A, p, r):
        ram = random.randrange(p, r)
        A[r], A[ram] = A[ram], A[r]
        pivot = A[r]
        i = p-1
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def median_parition(A, p, r):
        ram = random.sample(range(p, r+1), 3)
        mid = 
        A[r], A[mid] = A[mid], A[r]
        pivot = A[r]
        i = p-1
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

# NG quicksort that ignores equal elements
class quick_sort2(A):
    def quicksort(A, p, r):
    # recursive call on quicksort
        if p < r:
            q = partition(A, p, r)[0]
            t = partition(A, p, r)[1]
            quicksort(A, p, q-1)
            quicksort(A, t+1, r)

    def ram_partition(A, p, r, t):
        ram = random.randrange(p, r)
        A[r], A[ram] = A[ram], A[r]
        pivot = A[r]
        i = t = p-1
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        
        return [i+1, t] 

# NG
class fuzzy_sort(A):
    def fuzzysort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            fuzzysort(A, p, q-1)
            fuzzysort(A, q+1, r)

    def intersect(a, b):
        if a[0] <= b[1] and b[0] <= a[1]:
            # a intersects b
            return 0
        elif a[1] < b[0]:
            # a is before b
            return -1
        elif a[0] > b[1]:
            # a is after b
            return 1

    def parition(A, p, r):
        ram = random.randrange(p, r)
        A[r], A[ram] = A[ram], A[r]
        pivot = A[r]
        i = p-1
        for j in range(p, r):
            if intersect(A[j], pivot): 
            A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1