# Author: Alexandre Brilhante

''' 8 Queens problem using backtracking. '''

def queensBT(sol, k, col, diag45, diag135):
    if k == 8:
        return sol
    else:
        for j in range(0, 8):
            if not (j in col and (j-k) in diag45 and (j+k) in diag135):
                sol += [j]
                return queensBT(sol, k+1, col+[j], diag45+[j-k], diag135+[j+k])

print(queensBT([], 0, [], [], []))