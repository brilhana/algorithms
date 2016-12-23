# Author: Alexandre Brilhante

''' Solves graph coloring using 3 colors. '''

def color(M, col):
    if not promising(M, col):
        return False
    elif promising(M, col) and len(col) == len(M):
        return True
    else:
        for c in ['Blue', 'Green', 'Red']:
            if color(M, col+[c]):
                return True
        return False

def promising(M, col):
    for i in range(0, len(col)):
        for j in range(0, len(col)):
            if M[i][j] and col[i] == col[j]:
                return False
    return True