'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics
'''

#bucket sort
#assume the input is generated randomly with uniform distribution elements
import math

def bucket_sort(A):
    # create a new empty array B
    n = len(A)
    B = [[] for _ in range(n)]

    def insertion_sort(A):
        for i in range(len(A)):
            key = A[i]
            j = i - 1
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j = j - 1
            A[j+1] = key
        return A

    #insert A[i] into list B[floor(nA[i])]
    for i in range(n):
        index = int(math.floor(n*A[i] - 1))
        B[index].append(A[i])
        
    for i in range(n):
        if len(B[i]) > 0:
            insertion_sort(B[i])
            print B[i]
    
    #flatten list B
    flat_list = [item for sublist in B for item in sublist]
    return flat_list

A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print bucket_sort(A)



