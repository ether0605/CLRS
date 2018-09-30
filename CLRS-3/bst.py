'''
Written:       2018/09/19
Last updated:  2018/09/20
Language: Python

Introduction to Algorithm: III Data Structure

12 Binary Search Tree

Implementation of a binary search tree
'''

import random

class Node(object):
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.p = None

class BSTree(object):
	def __init__(self, Node):
		self.root = Node

	def search(self, target):
		while self.key != None and self.key != target:
			if k < self.key:
				self = self.left
			else:
				self = self.right
		return self

	def inorder_walk(self):
		if self.key != None:
			inorder_walk(self.left)
			print (self.key)
			inorder_walk(self.right)

	def preorder_walk(self, A):
		if self.key != None:
			print (self.key)
			preorder_walk(self.left)
			preorder_walk(self.right)

	def minimum(self):
		while self.left != None:
			self = self.left
		return self.key

	def maximum(self):
		while self.right != None:
			self = self.right
		return self.key

	def successor(self, x):
		# the left most node in the right subtree
		if x.right != None:
			return self.minimum(x.right)
		# go up the tree from x until find a node that is the left child of its parent
		y = x.p
		while y != None and x == y.right:
			x = y
			y = y.p
		return y

	def insert(self, target):
		# two pointers, y tracks the parent root
		y = None
		# find the None position to insert target
		while self.key != None:
			y = self.p
			if target.key < self.key:
				self = self.left
			else: self = self.right
		# set the pointer
		target.p = y
		if y == None:
			# if the tree is empty
			self.root = target
		elif target.key < y.key:
			y.left = target
		else: y.right = target

	def sort(self, L):
		# random.shuffle list to get a randomized Tree
		for i in range(len(L)):
			self.insert(A[i])

	def transplant (self, u, v):
		# helper function for deletion: replace one subtree as a child of its parent with another subtree
		# replaces the subtree rooted at node u with the subtree rooted at node v; u.p become v.p
		if u.p == None:
			# when u is the root
			self.root = v
		
		elif u == u.p.left:
			# if u is a lft child
			u.p.left = v
		
		else:
			# if u is a right child
			u.p.right = v
		
		if v != None:
			# update v.p
			v.p = u.p

	def delete(self, target):
		# when target has no left child
		if target.left == None:
			self.transplant(target, target.right)
		# when target has no right child
		elif target.right == None:
			self.transplant(target, target.left)
		# when target has both
		else: 
			# find the successor of target
			y = self.minimum(target.right)
			# replace y as a child of its parent by y's right child, and target right child becomes y right child
			if y.p != target:
				self.transplant(y, y.right)
				y.right = target.right
				y.right.p = y
			# replace target as a child of its parent by y and replace y's left child by z left child
			self.transplant(target, y)
			y.left = target.left
			y.left.p = y

# test case
A = []
s = random.randint(5, 20)
for i in range(0, s):
    A.append(Node(random.randint(0, 100)))
k = random.choice(A)
t = BSTree()
t.sort(A)
t.inorder_walk()
# print ("Search", k, " :", t.search(k).key)
# print ("Finding the Minimum elem :", t.minimum())
# print ("Finding the Maximum elem :", t.maximum())
# d = random.choice([A[i].key for i in range(len(A))])
# print ("we are going to delete:",d)
# t.delete(t.search(d))
# B = []
# t.inorder_walk(B)
# print ("After deletion:",[B[i].key for i in range(0, len(B))])