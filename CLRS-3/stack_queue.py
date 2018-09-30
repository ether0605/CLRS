'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: III Data Structure

10.1 stack and queue

basic structure of stack and queue
python collections module: 
from collections import deque
'''

class Stack(object):
	def __init__(self, n):
		self.items = []

	def is_empty(self):
		if len(self.items) == 0:
			return True
		return False

	def push(self, x):
		self.items.append(x)

	def pop(self):
		if self.is_empty():
			raise "underflow"
		else:
			S.pop()

class Queue(object):
	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		self.queue.insert(0, val)

	def dequeue(self):
		if self.is_empty():
			raise"underflow"
		else:
			self.self.pop(0)

	def is_empty(self):
		return True if len(self)>0 else False
		