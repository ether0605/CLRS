'''
Written:       2018/08/31
Last updated:  2018/09/03
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics
'''

#Heapsort, max, using recursion
class heap_sort(A):
    def max_heapify(A, i, heap_size):
    # maintain the max-heap property
        left = (i+1)*2 - 1
        right = (i+1)*2
        largest = i
        if left < heap_size and A[left] > A[i]:
            largest = left
        if right < heap_size and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            max_heapify(A, largest, heap_size)

    def build_max_heap(A, heap_size):
    # goes through the nodes of the tree and calls max_heapify on each note
        for i in range(len(A)/2-1, -1, -1):
            max_heapify(A, i, heap_size)

    def heapsort(A):
    # sort an array in place
        heap_size = len(A)
        build_max_heap(A, heap_size)
        for i in range(1, len(A)):
            A[0], A[-i] = A[-i], A[0]
            heap_size -= 1
            max_heapify(A, 0, heap_size)
        return A

    #implement the operations of a max-priority queue
    def max_heap_insert(A, key): 
        A.append(key)

    def heap_extract_max(A, heap_size):
        if heap_size < 1:
            "heap underflow"
        maxnum = A[0]
        A[0] = A[heap_size]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        return maxnum

    def heap_increase_key(A, i ,key):
        if key < A[i]:
            print "new key is smaller than current key"
        A[i] = key
        while i > 0 and A[i/2] < A[i]:
            A[i], A[i/2] = A[i/2], A[i]
            i = i/2

    def heap_max(A):
        return A[0]
