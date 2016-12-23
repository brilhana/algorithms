# Author: Alexandre Brilhante

''' Solves the knapsack problem using greedy approach, dynamic programming and backtracking. '''

def knapsackGreedyContinuous(items, W):
    items = sorted(((v/w, w) for w, v in items), reverse = True)
    wt  = 0
    val = 0
    for value, weight in items:
        if wt <= W:
            portion = min(W-wt, weight)
            wt  += portion
            val += portion*value
    return val

def knapsackDP(items, W):
    T = [[0 for x in range(W+1)] for y in range(len(items)+1)]
    for i in range(0, len(items)+1):
        for j in range(1, W+1):
            if i == 0:
                T[i][j] = 0
            elif items[i-1][0] <= j:
                T[i][j] = max(T[i-1][j], items[i-1][1]+T[i-1][j-items[i-1][0]])
            else:
                T[i][j] = T[i-1][j]
    return T[-1][-1]

def knapsackDPMult(items, W):
    T = [[0 for x in range(W+1)] for y in range(len(items)+1)]
    for i in range(0, len(items)+1):
        for j in range(1, W+1):
            if i == 0:
                T[i][j] = 0
            elif items[i-1][0] <= j:
                T[i][j] = max(T[i-1][j], items[i-1][1]+T[i-1][j-items[i-1][0]], items[i-1][1]+T[i][j-items[i-1][0]])
            else:
                T[i][j] = T[i-1][j]
    return T[-1][-1]

def knapsackBT(items, i, W):
    val = 0
    for k in range(i, len(items)):
        if items[k][0] <= W:
            val = max(val, items[k][1]+knapsackBT(items, k, W-items[k][0]))
    return val