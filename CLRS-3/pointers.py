'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: III Data Structure

10.3 pointers and objects

implementation of pointers and objects
'''

class Pointer(object):
	def __init__(self, key, prev=None, next=None):
		self.key = key
        self.next = next
        self.prev = prev

    def get_ptr(self):
    	return self.key