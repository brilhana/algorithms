# Author: Alexandre Brilhante

''' Brute-force knapsack. '''

items = [("object 1", 1.0, 3.0),
         ("object 2", 2.0, 4.0),
         ("object 3", 4.0, 4.0),
         ("object 4", 4.0, 5.0),
         ("object 5", 4.0, 2.0)]

def knapsack(items, W):
    sorted_items = sorted(((value/weight, weight, name) for name, weight, value in items), reverse = True)
    wt = val = 0
    bagged = []
    for unit_value, weight, name in sorted_items:
        portion = min(W - wt, weight)
        wt     += portion
        val    += portion * unit_value
        bagged += [(name, portion, portion * unit_value)]
        if wt >= W:
            break
    return wt, val
