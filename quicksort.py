# Author: Alexandre Brilhante

''' Quicksort using random pivot. '''

import random

def quicksort(T):
    if len(T) <= 1:
        return T
    pivot = random.choice(T)
    less  = [x for x in T if x <  pivot]
    equal = [x for x in T if x == pivot]
    more  = [x for x in T if x >  pivot]
    return quicksort(less) + equal + quicksort(more)
