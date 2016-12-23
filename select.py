# Author: Alexandre Brilhante

''' Selects and returns the kth smallest element using a divide and conquer. '''

from math import ceil
from random import randint
from statistics import median

def selection(T, k):
    if len(T) <= 5:
        return sorted(T)[k]
    else:
        p = T[randint(0, len(T))]
        U = [x for i in T if x <  p]
        V = [x for i in T if x <= p]
        if k <= len(U):
            return selection(U, k)
        elif k <= len(V):
            return p
        else:
            return selection(V, k-len(V))

def pseudomedian(T):
    if len(T) <= 5:
        return median(T)
    else:
        z = len(T)//5
        M = [0]*z
        for i in range(0, z):
            M[i] = median(T[5*i-4:5*i])
    return selection(M, ceil(z/2))