# Author: Alexandre Brilhante

''' Levenstein's distance between two strings using dynamic programming. '''

def levenstein(u, v):
	D = [[0]*(len(v)+1) for i in range(len(u)+1)]
	for i in range(len(u)+1):
		D[i][0] = i
	for j in range(len(v)+1):
		D[0][j] = j
	for i in range(1, len(u)+1):
		for j in range(1, len(v)+1):
			b = 1 if u[i] != v[j] else 0
			D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+b)
	return D[-1][-1]