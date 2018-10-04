'''
Written:       2018/10/02
Last updated:  -
Language: Python

Introduction to Algorithm: IV Advanced Design and Analysis Techniques

15 Dynamic Programming

Implementation of some dynamic programming algorithms
'''

# Cut-Rod Problem
def cutRod(p, n):
	r = [0*_ for _ in range(n+1)]
	s = [0*_ for _ in range(n+1)]
	res = []
	p.insert(0, 0)
	for j in range(1, n+1):
		for i in range(1, j+1):
			if r[j] < p[i] + r[j-i]:
				r[j] = p[i] + r[j-i]
				s[j] = i
	while n > 0:
		res.append(s[n])
		n -= s[n]
	return r[-1], res

p = [1, 5, 8, 9, 10]
n = 5
#print (cutRod(p, 5))


