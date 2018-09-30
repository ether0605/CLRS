'''
Written:       2018/09/12
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: III Data Structure

10.2 linked lists

implementation of linked lists
'''
class Node(object):
    def __init__(self, value = None, next = None, prev = None):
        self.val = value
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

class Linked_List(object):
    def __init__(self):
        self.head = None
        self.prev = None

    #insert item x into the front of the list
    def insert(self, x):
        if self.head != None:
            new = Node(x, self.head, self.head.prev)
            self.head.prev = new
        else:
            new = Node(x, self.head, None)
        self.head = new

    def search(self, k):
        key = self.head
        while key!= None:
            if key.val == k:
                return key
            key = key.next
        return None

    def delete(self, x):
        node = self.search(x)
        if not node:
            return None
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next != None:
            node.next.prev = node.prev