# -*- coding: utf-8 -*-

'''
Written:       2018/10/04
Last updated:  -
Language: Python

Introduction to Algorithm: IV Advanced Design and Analysis Techniques

16 Greedy Algorithms

Implementation of some greedy algorithms
'''

# activity selection problem
def activity_selector(activity):
	'''
	input: a list of tuple(start time, finish time) for activities, 
	ordered increasingly by finish time
	return: index of selected activities
	'''
	ac = activity
	n = len(ac)
	selected = [0]
	s = 0
	for i in range(1, n):
		if ac[i][0] > ac[s][1]:
			selected.append(i)
			s = i
	return selected

# ac = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# print activity_selector(ac)


