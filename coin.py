# Author: Alexandre Brilhante

''' Coin change problem using greedy approach and dynamic programming. '''

def changeGreedy(coins, k):
    coins = sorted(coins, reverse = True)
    total = 0
    result = 0
    for c in coins:
        if c+total <= k:
            total  += c
            result += 1
    return result

def changeDP(coins, k):
    T = [[0]*(k+1) for i in range(len(coins))]
    for i in range(0, len(coins)):
        for j in range(1, k+1):
            a = T[i-1][j]        if i > 0         else float("inf")
            b = T[i][j-coins[i]] if j >= coins[i] else float("inf")
            T[i][j] = min(a, b+1)
    return T[-1][-1]