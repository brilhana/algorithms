# Author: Alexandre Brilhante

from math import ceil, floor, log2

''' Returns u*v using a divide and conquer algorithm. '''

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

def multiply(u, v):
    if len(str(u)) == 1 or len(str(v)) == 1:
        return u*v
    elif len(str(u)) == len(str(v)):
        s = len(str(u)) // 2
        w, x = u // (10**s), u % (10**s)
        y, z = v // (10**s), v % (10**s)
        return add(multiply(w, y) * (10**(2*s)), add(multiply(w, z), add(multiply(x, y) * (10**s), multiply(x, z))))
