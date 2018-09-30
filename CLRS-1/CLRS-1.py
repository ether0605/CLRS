'''
Written:       2018/08/28
Last updated:  2018/08/31
Language: Python

Introduction to Algorithm: I Foundation
'''

#pset 2.1-3 linear search
def linear_serach(A, target):
    for i in A:
        if i == target:
        	return True
    return False

#pset 2.2-2 selection_sort
def selection_sort(A):
    for i in range(len(A)):
        imin = i
        j = i
        while j < len(A):
            if A[j] < A[imin]:
                imin = j
            j += 1
        A[i], A[imin] = A[imin], A[i]
    return A

#merge_sort
def merge(Left, Right):
    len1 = len(Left)
    len2 = len(Right)
    result = [0] * (len1 + len2)
    i = j = k = 0
    
    for k in range(len1 + len2):      
        if i < len1 and j < len2:
            if Left[i] <= Right[j]:
                result[k] = Left[i]
                i += 1
            else:
                result[k] = Right[j]
                j += 1
        else: break
            
    while i < len1:
        result[k] = Left[i]
        i += 1
    while j < len2:
        result[k] = Right[j]
        j += 1
    return result

def merge_sort(A):
    if len(A) < 2:
        return A
    else:
        mid = len(A)/2
        Left = merge_sort (A[:mid])
        Right = merge_sort (A[mid:])
        return merge(Left, Right)
    

# pset 2.3-4 recursive of insertion sort
# 	def insertion_sort2(A, n=0):
# 		if n < len(A):
# 			insertion_sort2(A, n+1)

# 		temp = [0] * len(A)
# 		for i in range(n):
# 	        if A[i] > A[n]:
# 	        	temp[i+1:] = A[i:-1]
# 	        	temp[i] = A[-1]
# 	        	break
# 	    A = temp

#pset 2.3-5 binary search, assue A is sorted
def binary_search(A, target):
    if len(A) < 2:
        if not A:
            return False
        return target == A[0]
    else:
        mid = len(A)/2
        if target == A[mid]:
            return True
        elif target < A[mid]:
            return binary_search(A[:mid], target)
        else:
            return binary_search(A[mid:], target)

#p 2-2 bubble sort
def bubble_sort(A):
	for i in range(len(A)):
		for j in range(len(A)-i-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
	return A

#find the maximum-subarray using Divide and Conquer
def max_cross_array(A, left, mid, right):
	l_sum = r_sum = a_sum = 0
	max_l = max_r = mid
	for i in range(mid, left-1, -1):
		a_sum += A[i]
		if a_sum > l_sum:
			l_sum = a_sum
			max_l = i
	for i in range(mid+1, right+1):
		a_sum += A[i]
		if a_sum > r_sum:
			r_sum = a_sum
			max_r = i
	return (max_l, max_r, a_sum)

def max_subarray(A, left, right):
	L = R = C = []
	if left == right:
		return (left, right, A[left])
	else:
		mid = (left+right)/2
		L = max_subarray(A, left, mid)
		R = max_subarray(A, mid+1, right)
		C = max_cross_array(A, left, mid, right)
		if L[2] >= R[2] and L[2] >= C[2]:
			return L
		elif R[2] >= L[2] and R[2] >= C[2]:
			return R
		else:
			return C
