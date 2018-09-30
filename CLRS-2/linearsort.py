'''
Written:       2018/09/03
Last updated:  2018/09/12
Language: Python

Introduction to Algorithm: II Sorting and Order Statistics
'''

#linear sort

def counting_sort(A, k):
# all intergers in A falls in [0, k], B is the output list
    C = [0] * (k+1)
    B = [0] * len(A)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A), 0, -1):
        B[C[A[j-1]]-1] = A[j-1]
        C[A[j-1]] -= 1
    return B

'''If the items to be sorted are Integers with large range but of few digits, 
we can combine Counting Sort idea with Radix Sort to achieve the linear time complexity.
Items are sorted backward (rightmost digit)'''
def radix_sort(A, d):
# each element in the n-element array A has d digits
    D = empty = {}
    a_str = A[:]       
    for num in range(d):
        for i in range(10):
            D[i] = [] 
        for item in a_str:
            D[item // 10**num % 10].append(item)
        a_str = []
        for k, v in D.items():
            if len(v) > 0:
                D[k] = counting_sort(v, 60)
                a_str.extend(D[k])
    return a_str

#A = [29, 57, 39, 36, 20, 55]


