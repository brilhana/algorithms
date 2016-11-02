# Author: Alexandre Brilhante

''' Merge sort. '''

def mergesort(T):
    if len(T) <= 1:
        return T
    U = T[:len(T)//2]
    V = T[len(T)//2:]
    U = mergesort(U)
    V = mergesort(V)
    return merge(U, V)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result
