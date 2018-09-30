'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: III Data Structure

10.4 rooted tree

implementation of rooted tree
'''

class Rooted_Tree(object):
	def __init__(self, key, child=[], sibling=[], parent=[]):
		self.key = key
		self.child = child
		self.sibling = sibling
		self.parent = parent

	def add_child(self, x):
		self.child.append(x)

	def add_sibling(self, x):
		self.child.append(x)

	def get_parent(self):
		return self.parent