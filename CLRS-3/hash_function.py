'''
Written:       2018/09/13
Last updated:  2018/09/13
Language: Python

Introduction to Algorithm: III Data Structure

11 Hash Tables

11.3 Hash Functions - 
Division Method, Multiplication Method and Universal Hashing
'''

import math

# m slots, not too close to 2^p
def hash_div(key, m):
	return key % m

def hash_mul(key, m):
	constant = 0.618034
	return math.floor(m*(key*constant%1))

