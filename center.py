# Author: Alexandre Brilhante

''' Returns the center of a graph. '''

def floyd(G):
    A = G
    for k in range(0, len(G)):
        for i in range(0, len(G)):
            for j in range(0, len(G)):
                A[i][j] = min(G[i][j], G[i][k]+G[k][j])
    return A

def excentricity(L):
    E = [0]*len(L)
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            E[i] = max(E[i], L[j][i])
    return E

def center(G):
    L = floyd(G)
    E = excentricity(L)
    c = 1
    for v in range(1, len(E)):
        if E[v-1] <= E[v]:
            c = v
    return c

print(center(G))
