'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics

9.1
simultaneous min and max, o(n) and at most 3[n/2] comparisons
'''

def min_max(A):
	n = len(A)
	if n % 2 != 0:
		minA = maxA = A[0]
	else:
		minA, maxA = min(A[0], A[1]), max(A[0], A[1])
		A.pop(0)

	# compare the rest elements in pairs, then compare smaller with minA, larger with maxA
	i = 1
	while i < n:
		tempmin = A[i]
		tempmax = A[i+1]
		if A[i] > A[i+1]:
			tempmin, tempmax = tempmax, tempmin
		if tempmin < minA:
			minA = tempmin
		if tempmax > maxA:
			maxA = tempmax

		i += 2

	return (minA, maxA)



