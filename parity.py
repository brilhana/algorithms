# Author: Alexandre Brilhante

''' Returns true if m is even, odd otherwise, using greedy approach and divide and conquer. '''

def parity(m):
    if m == 0:
        return True
    elif m == 1:
        return False
    else:
        return parity(m-2)

def parityDC(m):
    if m == 0:
        return True
    elif m == 1:
        return False
    else:
        i = 0
        j = len(str(m))
        while i < j:
            i += 1
            j -= 1
        return parityDC(int(format(i, 'b'))) == parityDC(int(format(j, 'b')))