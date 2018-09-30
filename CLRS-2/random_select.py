'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics

9.2 random select
divide and conquer

returns the ith smallest element of the array A, assumming elements are distinct
'''


import random

# helper: randomized_partition
def helper(A, p, r):
	# the result went wrong with ram select
    #ram = random.randrange(p, r)
    #A[r], A[ram] = A[ram], A[r]
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

#p:start index, r:end index, ith smallest element
def randomized_select(A, p, r, i):
	if p == r:
		return A[p]
	q = helper(A, p, r)
	k = q - p

	# the pivot the element A[q] is the answer
	if i == k:
		return A[q]

	elif i < k:
		return randomized_select(A, p, q-1, i)
	else:
		return randomized_select(A, q+1, r, i - k)


