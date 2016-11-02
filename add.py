# Author: Alexandre Brilhante

from math import floor, log2

''' Returns a+b using a divide and conquer algorithm. '''

def add(a, b):
    if a < 4 and b < 4:
        return a + b
    else:
        m = int(floor(log2(max(a,b)))+1)
        shift = m // 2
        r = 2**shift
        s, t = a // r, a % r
        v, w = b // r, b % r
        return ((r * add(s, v)) + add(t, w))
