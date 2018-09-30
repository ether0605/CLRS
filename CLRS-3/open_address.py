'''
Written:       2018/09/13
Last updated:  2018/09/13
Language: Python

Introduction to Algorithm: III Data Structure

11 Hash Tables

11.3 Open addressing - 
Linear probing, quadratic probing, double hashing
'''

import math

class Linear_Probing(object):
    def __init__(self, m=0):
        self.hash = {}
        self.size = m

    def __str__(self):
    	dic = {k: v for k, v in self.hash.items() if v != None}
    	return str(dic)

    def helper(self, key):
        return key % self.size

    def insert_list(self, A):
        for i in A:
            self.insert(i)

    def insert(self, key):
        pos = self.helper(key)
        for i in range(self.size):
            slot = (pos + i)%self.size
            if slot not in self.hash.keys() or self.hash[slot] == None:
                self.hash[slot] = key
                break

    def search(self, key):
        pos = self.helper(key)
        for i in range(self.size):
            slot = pos + i
            if slot not in self.hash.keys():
                return "key not exist"
            elif self.hash[slot] == key:
                return slot

    def delete(self, key):
        find = self.search(key)
        if find:
            self.hash[find] = None
        else:
            return "key not exist"
            
class Quadratic_Probing(object):
    def __init__(self, m):
        self.hash = {}
        self.size = m

    def helper(self, key):
        return key % self.size

    def insert_list(self, A):
        for i in A:
            self.insert(i)

    def insert(self, key):
        pos = self.helper(key)
        c1 = 1
        c2 = 3
        for i in range(self.size):
            slot = (pos + c1 * i + c2 * i * i) % self.size
            if slot not in self.hash.keys():
            	self.hash[slot] = key
                break
            if i == self.size:
                raise 'hash table overflow'
        

class Double_hashing(object):
	def __init__(self, m):
		self.hash = {}
		self.size = m

	def helper1(self, key):
		return key % self.size

	def helper2(self, key):
		return 1 + key % (self.size - 1)

	def insert_list(self, A):
		for i in A:
			self.insert(i)

	def insert(self, key):
		slot1 = self.helper1(key)
		slot2 = self.helper2(key)
		for i in range(self.size):
			slot = (slot1 + i * slot2)%self.size
			if len(self.hash.keys()) == self.size:
				raise 'overflow'
			elif slot in self.hash.keys():
				continue
			else:
				break
		self.hash[slot] = key
