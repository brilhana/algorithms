# Author: Alexandre Brilhante

''' Selects and returns the kth smallest element. '''

def select(T, k):
    for i in range(0, len(T)):
        min_index = i
        min_value = T[i]
        for j in range(i+1, len(T)):
            if T[j] < min_value:
                min_index = j
                min_value = T[j]
        T[i], T[min_index] = T[min_index], T[i]
    return T[k]
